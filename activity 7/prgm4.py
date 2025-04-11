def count_good(feedback):
    count = feedback.lower().count("good")
    print(f"The word 'good' appears {count} times.")
count_good("The service was Good, very GOOD and just overall good!")
