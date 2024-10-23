import pickle  # Make sure to import the pickle module

try:
    with open(r"C:\Users\keert\Desktop\miniprojectexe\miniproject\prediction.pkl", 'rb') as f:
        rf_model = pickle.load(f)
    print("Model loaded successfully!")
except pickle.UnpicklingError as e:
    print("Error loading the model:", e)
except FileNotFoundError as e:
    print("Pickle file not found:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
