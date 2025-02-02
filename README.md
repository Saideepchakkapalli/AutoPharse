Project Title: Auto-Phrase
Overview:
       Auto-Phrase is a smart text assistant that helps users by providing spelling corrections and predicting the next words in their sentences. It uses machine   
       learning models to enhance the writing experience, making it smoother and more accurate.

1.Key Features:
**Spelling Autocorrect:
            * Automatically detects and suggests corrections for misspelled words.
            * Ensures that users enter correctly spelled words before moving forward.

**Next Word Prediction:
            * Predicts the next 2-3 possible words based on the text entered so far.
            * Helps users complete their sentences quickly and accurately.
**Fluency Evaluation:
            * Analyzes the entered sentence and provides a fluency score.
            * Offers insights into the fluency of the text, encouraging better writing.
2.How It Works:
**Input Handling:
       * As the user types, the system checks each word when the spacebar is pressed.
       * If a word is incorrect, the system displays suggested corrections.
       * If the word is correct, the system provides predictions for the next possible words.
**Fluency Scoring:
      * When the Enter key is pressed, the system evaluates the fluency of the entire sentence.
      * A score is displayed below the suggestions, indicating the quality of the text.
      
3.Technology Stack:
**Frontend:
          * HTML, CSS, and JavaScript for the user interface.
          * Responsive design with a visually appealing gradient background.
**Backend:
          * Flask framework for the server.
          * Machine learning models for autocorrection and next word prediction.
          * TensorFlow and Keras for model implementation.
          * Pandas and Textdistance for data processing and similarity calculations.
          
4.User Interaction :
**Typing and Corrections:
          * Users type their text into a text area.
          * The system detects and suggests corrections for misspelled words in real-time.
          * If the word is correct, the system predicts the next words to help complete the sentence.
**Fluency Feedback:
          * By pressing Enter, users can get an instant fluency score for their sentence.
          * This helps users understand the readability and flow of their writing.
5.Benefits:
          * Efficiency: Speeds up the writing process by providing real-time suggestions and predictions.
          * Accuracy: Ensures correct spelling and improves sentence structure.
          * Feedback: Offers immediate feedback on the fluency of the text, helping users improve their writing skills.
