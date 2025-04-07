from oop.lazy_import import Student, Compute

if __name__ == '__main__':
    s1 = Student("rss", 50)
    s2 = Student("gsx", 60)

    c = Compute()
    total = c.add(s1.get_score(), s2.get_score())
    print(f"{total=}")
