from seasons import minutes_lived,num_words

def main():
    test_num_words()

def test_num_words():
    assert num_words(minutes_lived(1999,1,1)).capitalize() == "Twelve million, eight hundred forty-seven thousand, six hundred eighty"
    assert num_words(minutes_lived(2000,2,2)).capitalize() == "Twelve million, two hundred seventy-six thousand"
   


if __name__ == "__main__":
    main()