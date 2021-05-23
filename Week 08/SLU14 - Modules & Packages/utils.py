import hashlib
import json

def encode_answer(answer):
    encoded_answer = hashlib.sha256(json.dumps(answer).encode()).hexdigest()
    return encoded_answer
    
q1 = "879923da020d1533f4d8e921ea7bac61e8ba41d3c89d17a4d14e3a89c6780d5d"
q2 = "3fa5834dc920d385ca9b099c9fe55dcca163a6b256a261f8f147291b0e7cf633"
q3 = "c100f95c1913f9c72fc1f4ef0847e1e723ffe0bde0b36e5f36c13f81fe8c26ed"
q4 = "879923da020d1533f4d8e921ea7bac61e8ba41d3c89d17a4d14e3a89c6780d5d"
q5 = "c100f95c1913f9c72fc1f4ef0847e1e723ffe0bde0b36e5f36c13f81fe8c26ed"
q8 = "c100f95c1913f9c72fc1f4ef0847e1e723ffe0bde0b36e5f36c13f81fe8c26ed"
q9 = "ac8d8342bbb2362d13f0a559a3621bb407011368895164b628a54f7fc33fc43c"
q10 = "3fa5834dc920d385ca9b099c9fe55dcca163a6b256a261f8f147291b0e7cf633"
q11 = "c100f95c1913f9c72fc1f4ef0847e1e723ffe0bde0b36e5f36c13f81fe8c26ed"
