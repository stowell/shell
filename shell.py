import os


def messages():
    while True:
        try:
            message = raw_input('> ')
            yield message
        except EOFError:
            raise StopIteration
        except KeyboardInterrupt:
            continue


class Error(object):
    def __init__(self, error_message):
        self.error_message = error_message

    def next_word(self, word):
        return self

    def evaluate(self, environment):
        return (environment, self.error_message)


class Empty(object):
    def next_word(self, word):
        if 'list' == word:
            return List()
        else:
            return Error("sorry, i don't know '%s'" % word)

    def evaluate(self, environment):
        return (environment, '')


class List(object):
    def next_word(self, word):
        return Error("sorry, list doesn't take any more words")

    def evaluate(self, environment):
        return (environment, os.listdir(os.getcwd()))


class Environment(object):
    pass


def append_to_db(message, expression, environment, value):
    pass


def main():
    environment = Environment()
    for message in messages():
        expression = Empty()
        words = message.split()
        for word in words:
            expression = expression.next_word(word)
        new_environment, value = expression.evaluate(environment)
        append_to_db(message, expression, environment, value)
        print value


if __name__ == '__main__':
    main()
