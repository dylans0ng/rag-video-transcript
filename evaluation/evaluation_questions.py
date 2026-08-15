EVALUATION_QUESTIONS = [
    # DIRECT QUESTIONS
    {
        "question": "How do I install the OpenAI Python package?",
        "category": "direct",
        "answerable": True,
        "expected_topic": "installing the OpenAI package",
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_3',
            'ai-python-vid-1-transcript_chunk_4'
        ]
    },  
    {
        "question": "How do I create an OpenAI client in Python?",
        "category": "direct",
        "answerable": True,
        "expected_topic": "creating the OpenAI client",
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_5'
        ]
    },
    {
        "question": "How do I send a prompt to an OpenAI model?",
        "category": "direct",
        "answerable": True,
        "expected_topic": "making an OpenAI API request",
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_7',
            'ai-python-vid-1-transcript_chunk_8',
            'ai-python-vid-1-transcript_chunk_9',
            'ai-python-vid-1-transcript_chunk_10',
            'ai-python-vid-1-transcript_chunk_11',
            'ai-python-vid-1-transcript_chunk_12',
            'i-python-vid-1-transcript_chunk_14'
        ]
    },
    {
        "question": "Where should I store my OpenAI API key?",
        "category": "direct",
        "answerable": True,
        "expected_topic": "storing the API key in a .env file",
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_5',
            'ai-python-vid-1-transcript_chunk_6'
        ]
    },

    # PARAPHRASED QUESTIONS
    {
        "question": "How can Python communicate with an AI model?",
        "category": "paraphrased",
        "answerable": True,
        "expected_topic": "calling an AI model through the OpenAI API",
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_1',
            'ai-python-vid-1-transcript_chunk_5',
            'ai-python-vid-1-transcript_chunk_7'
        ]
    },
    {
        "question": "How can I keep my secret key out of my Python code?",
        "category": "paraphrased",
        "answerable": True,
        "expected_topic": "using environment variables and a .env file",
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_6'
        ]
    },
    {
        "question": "How can user input be inserted into an AI prompt?",
        "category": "paraphrased",
        "answerable": True,
        "expected_topic": "building a dynamic user prompt",
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_9',
            'ai-python-vid-1-transcript_chunk_10',
            'ai-python-vid-1-transcript_chunk_11',
            'ai-python-vid-1-transcript_chunk_12',
            'ai-python-vid-1-transcript_chunk_14',
            'ai-python-vid-1-transcript_chunk_15'
        ]
    },

    # SPECIFIC-DETAIL QUESTIONS
    {
        "question": "Why does the video create a virtual environment?",
        "category": "specific_detail",
        "answerable": True,
        "expected_topic": "isolating project dependencies",
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_2',
            'ai-python-vid-1-transcript_chunk_3'
        ]
    },
    {
        "question": "What is the purpose of the requirements.txt file?",
        "category": "specific_detail",
        "answerable": True,
        "expected_topic": "recording project dependencies",
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_4'
        ]
    },
    {
        "question": "What file is used to store environment variables?",
        "category": "specific_detail",
        "answerable": True,
        "expected_topic": ".env file",
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_5'
        ]
    },
    {
        "question": "Does the AI model automatically remember previous API calls?",
        "category": "specific_detail",
        "answerable": True,
        "expected_topic": "API calls are stateless",
        "expected_chunk_ids": []
    },

    # BROAD QUESTIONS
    {
        "question": "What are the main steps required to call an AI model from Python?",
        "category": "broad",
        "answerable": True,
        "expected_topic": (
            "setting up the environment, installing packages, configuring "
            "the API key, creating the client, and sending a prompt"
        ),
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_1',
            'ai-python-vid-1-transcript_chunk_2',
            'ai-python-vid-1-transcript_chunk_3',
            'ai-python-vid-1-transcript_chunk_4',
            'ai-python-vid-1-transcript_chunk_5',
            'ai-python-vid-1-transcript_chunk_6',
            'ai-python-vid-1-transcript_chunk_7',
            'ai-python-vid-1-transcript_chunk_8',
            'ai-python-vid-1-transcript_chunk_10',
            'ai-python-vid-1-transcript_chunk_11',
            'ai-python-vid-1-transcript_chunk_12'
            ]
    },
    {
        "question": "What does the video teach about building prompts dynamically?",
        "category": "broad",
        "answerable": True,
        "expected_topic": "using user input to create a dynamic prompt",
        "expected_chunk_ids": [
            'ai-python-vid-1-transcript_chunk_14',
            'ai-python-vid-1-transcript_chunk_15'
        ]
    },

    # UNANSWERABLE QUESTIONS
    {
        "question": "How do I build a RAG system with ChromaDB?",
        "category": "unanswerable",
        "answerable": False,
        "expected_topic": None,
        "expected_chunk_ids": []
    },
    {
        "question": "How do I fine-tune an OpenAI model on my own dataset?",
        "category": "unanswerable",
        "answerable": False,
        "expected_topic": None,
        "expected_chunk_ids": []
    }
]