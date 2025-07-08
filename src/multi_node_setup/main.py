from src.multi_node_setup.graph import app

state = app.invoke({"name": "Tuhin", "age": "38", "skills": ["java", "python", "langgraph"]})
print(state["final"])

png_data = app.get_graph().draw_mermaid_png()

# Specify the output filepath
out_file = "output/graph.png"

# Write to disk
with open(out_file, "wb") as f:
    f.write(png_data)

print(f"Saved graph image to {out_file}")