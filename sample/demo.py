import aimodels

def main():
    llm = aimodels.openai.OpenAI("api_key", "model")

    print(llm.generate_text("prompt"))

if __name__ == "__main__":
    main()