import gradio as gr
import whisper
from language_tool_python import LanguageTool

# Load models
model = whisper.load_model("base")
tool = LanguageTool('en-US')

def transcribe_grammar(audio_path):
    result = model.transcribe(audio_path)
    text = result["text"]
    matches = tool.check(text)
    grammar_score = max(0, 10 - len(matches))
    sample_issues = [(m.ruleId, m.message) for m in matches[:5]]
    return text, grammar_score, sample_issues

iface = gr.Interface(
    fn=transcribe_grammar,
    inputs=gr.Audio(type="filepath"),
    outputs=["text", "number", "json"],
    title="Audio Grammar Checker",
    description="Upload a .wav file, and this app will transcribe it and give a grammar score."
)

iface.launch(share=True)