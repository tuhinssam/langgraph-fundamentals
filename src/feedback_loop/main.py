from src.feedback_loop.graph import app

print("===========LangGraph Feedback Loop===========")
state = app.invoke({"name": "Tuhin", "numbers": [], "counter": -1})

png_data = app.get_graph().draw_mermaid_png()

# Specify the output filepath
out_file = "output/graph.png"

# Write to disk
with open(out_file, "wb") as f:
    f.write(png_data)
    print(f"Saved graph image to {out_file}")