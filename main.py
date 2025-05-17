import os
import logging
from utils.grammar import check_grammar
from utils.readability import readability_score
from utils.ai_detector import detect_ai_content

# Setup logging
log_path = os.path.join("logs", "agent.log")
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(message)s')

def run_agent():
    print("Welcome to AI Linguist Agent")
    user_input = input("Enter the text to analyze:\n")

    print("\n📌 Checking grammar and style...")
    grammar_report = check_grammar(user_input)
    print(grammar_report)

    print("\n📊 Calculating readability score...")
    readability = readability_score(user_input)
    print(f"Readability Score: {readability}")

    print("\n🤖 Detecting if text is AI-generated...")
    ai_score = detect_ai_content(user_input)
    print(f"AI Detection Score: {ai_score:.4f} (Closer to 1 = AI-generated)")

    logging.info("Text analyzed | AI Score: %.4f | Readability: %.2f", ai_score, readability)

if __name__ == "__main__":
    run_agent()
