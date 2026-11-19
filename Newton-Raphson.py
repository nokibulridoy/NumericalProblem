# মূল ফাংশন: f(x) = x^3 - x^2 + 2
def func(x):
    return x * x * x - x * x + 2


# মূল ফাংশনের প্রথম ডেরিভেটিভ: f'(x) = 3x^2 - 2x
def derivFunc(x):
    return 3 * x * x - 2 * x


# Newton-Raphson Method দিয়ে Root বের করার ফাংশন
def newtonRaphson(x):

    # Newton-Raphson সূত্র অনুযায়ী h এর মান বের করা
    h = func(x) / derivFunc(x)

    # যতক্ষণ h এর পরম মান 0.0001 এর সমান বা বড় থাকবে
    while abs(h) >= 0.0001:

        # h এর নতুন মান বের করা
        h = func(x) / derivFunc(x)

        # নতুন x এর মান বের করা
        x = x - h

    # Root দশমিকের পর 4 ঘর পর্যন্ত প্রিন্ট করা
    print("The value of the root is :", "%.4f" % x)


# প্রোগ্রাম চালানোর জন্য প্রাথমিক মান নির্ধারণ
x0 = -20

# Newton-Raphson Function কল করা
newtonRaphson(x0)