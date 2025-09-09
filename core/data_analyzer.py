import io
import duckdb 
import base64
import pandasai as pai
import plotly.tools as tls
import matplotlib.pyplot as plt
from PIL import Image

from utils.llm import get_llm
# from utils.sanitize_code import sanitize_visualization_code

class DataAnalyzer:
    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file
        self.df = None
        self.llm = None
        self._initialize()

    def _initialize(self):
        try:
            self.llm = get_llm()
            pai.config.set({
                "llm": self.llm,
                "save_logs": True,
                "verbose": False,
                "open_charts": False,
            })
            self.df = self._load_file()
        except Exception as e:
            raise ValueError(f"Initialization failed: {str(e)}")

    def _load_file(self):
        try:
            if hasattr(self.uploaded_file, 'name') and hasattr(self.uploaded_file, 'getvalue'):
                filename = self.uploaded_file.name.lower()
                if filename.endswith(".csv"):
                    df = pai.read_csv(self.uploaded_file)

                elif filename.endswith((".xls", ".xlsx")):
                    df = pai.read_excel(self.uploaded_file)
                
                else:
                    raise ValueError(f"Unsupported file type: {filename}")
            else:
                raise ValueError("No valid file source provided")

            if hasattr(df, 'empty') and df.empty:
                raise ValueError("The file contains no data")
                
            return df
        except Exception as e:
            raise ValueError(f"Error loading file: {str(e)}")

    def analyze(self, query: str):
        if not query or not isinstance(query, str):
            raise ValueError("Invalid query")

        try:
            if len(query.strip()) < 2:
                return "Please provide a more specific question about your data."
            
            try:
                # instruction = (
                #     "If a visualization is needed, use Plotly Express to create an interactive figure, "
                #     "assign it to a variable named `result`, and do not save to file."
                # )
                # final_query = f"{query}\n\n{instruction}"
                response = self.df.chat(query)
                if hasattr(response, "_get_image"):
                    # code = response.last_code_executed
                    # safe_code = sanitize_visualization_code(code)

                    # try:
                    #     local_vars = {}
                    #     duckdb.register("table_from_bytes", self.df)
                    #     exec(safe_code, globals(), local_vars)
                    # except Exception as e:
                    #     print("[ERROR] Exec failed:", str(e))

                    # fig = plt.gcf()

                    # fig_plotly = tls.mpl_to_plotly(fig) 
                    # fig_plotly.update_layout(
                    #     width=600,
                    #     height=450, 
                    #     plot_bgcolor='white',
                    #     paper_bgcolor='white',
                    #     xaxis=dict(
                    #         title_font=dict(size=15, color='black'),
                    #         tickfont=dict(color='black'),
                    #     ),
                    #     yaxis=dict(
                    #         title_font=dict(size=15, color='black'),
                    #         tickfont=dict(color='black'),
                    #     )
                    # )
                    
                    b64_png = response.get_base64_image()        # str
                    img_bytes = base64.b64decode(b64_png)
                    image = Image.open(io.BytesIO(img_bytes))
                    
                    return {"type": "plot", "value": image}

                return {"type": "raw", "value": response}
            except Exception as e:
                return f"Error processing your query: {str(e)}"

        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
