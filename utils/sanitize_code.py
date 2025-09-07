import duckdb

def sanitize_visualization_code(code: str) -> str:
    lines = []
    for line in code.splitlines():
        if "execute_sql_query" in line:
            var_name = line.split("=")[0].strip()
            sql_var = line.split("(")[1].split(")")[0].strip()
            new_line = f"{var_name} = duckdb.query({sql_var}).to_df()"
            lines.append(new_line)
        else:
            if (
                "plt.savefig" in line
                or "plt.close()" in line
                or "plot_filename" in line
                or line.strip().startswith("result =")
            ):
                lines.append(f"# {line}")
            else:
                lines.append(line)

    return "\n".join(lines)