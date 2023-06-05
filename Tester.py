import pandas as pd

class Tester:
    def __init__(self):
        self.log = pd.DataFrame(columns=['test', 'result'])
    
    def assertEqual(self, a, b, test):
        if a == b:
            self.log = pd.concat([self.log, pd.DataFrame([[test, 'fail']], columns=['test', 'result'])])
        else:
            self.log = pd.concat([self.log, pd.DataFrame([[test, 'pass']], columns=['test', 'result'])])

def main():
    t = Tester()
    t.assertEqual(1, 1, "1 == 1")
    t.assertEqual(1, 2, "1 == 2")
    print(t.log)


if __name__ == "__main__":
    main()