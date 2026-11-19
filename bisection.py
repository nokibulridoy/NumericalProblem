# মূল ফাংশন
def func(x):
    return x*x*x - x*x + 2


# Bisection Method দিয়ে Root বের করার ফাংশন
def bisection(a, b):

    # a এবং b এর ফাংশনের মানের গুণফল 0 বা তার বেশি হলে
    # সঠিক Interval নির্বাচন করা হয়নি
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b")
        return

    # মাঝের বিন্দু বের করার জন্য
    c = a

    # যতক্ষণ পর্যন্ত b এবং a এর পার্থক্য 0.01 বা তার বেশি থাকবে
    while ((b-a) >= 0.01):

        # a এবং b এর মাঝের বিন্দু বের করা
        c = (a+b)/2

        # মাঝের বিন্দুতে ফাংশনের মান 0 হলে Root পাওয়া গেছে
        if (func(c) == 0.0):
            break

        # যদি c এবং a এর ফাংশনের মানের গুণফল 0 এর কম হয়
        # তাহলে Root a এবং c এর মাঝখানে আছে
        if (func(c)*func(a) < 0):
            b = c

        # অন্যথায় Root c এবং b এর মাঝখানে আছে
        else:
            a = c

    # Root দশমিকের পর 4 ঘর পর্যন্ত প্রিন্ট করবে
    print("The value of root is :", "%.4f" % c)


# প্রোগ্রাম চালানোর জন্য প্রাথমিক মান নির্ধারণ
a = -200
b = 300

# Bisection Function কল করা
bisection(a, b)