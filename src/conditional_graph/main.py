from src.conditional_graph.graph import app

png_data = app.get_graph().draw_mermaid_png()

# Specify the output filepath
out_file = "output/output_graph.png"

# Write to disk
with open(out_file, "wb") as f:
    f.write(png_data)

print(f"Saved graph image to {out_file}")

state = app.invoke({"number1": 11, "number2": 33, "operation": "+"})
print(state["final_number"])