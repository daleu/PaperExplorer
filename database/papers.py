import collections

class Paper:

    def __init__(self):
        self.citations = []
        self.title = ""
        self.author = ""
        self.date = ""

class Papers:
    CITATIONS_FILE = 'citations/hep-th-citations.txt'
    DATES_FILE = 'dates/hep-th-slacdates.txt'
    TITLES_FILE = 'abstract/titles.txt'
    AUTHORS_FILE = 'abstract/authors.txt'

    def __init__(self):
        self.papers = collections.defaultdict(Paper)

    def process_citations(self, file):

        print("Reading citations file at {0}".format(file))
        count = 0
        citations = collections.defaultdict(list)

        with open(file) as citations_file:
            for line in citations_file:
                line = line.rstrip()
                original, cite = line.split(' ')
                citations[original].append(cite)
                count += 1

        print("{0} citations were found\n".format(count))

        for key,value in citations.items():
            self.papers[key].citations = value

    def process_dates(self, file):

        print("Reading dates file at {0}".format(file))
        count = 0
        dates = collections.defaultdict(str)

        with open(file) as dates_file:
            for line in dates_file:
                line = line.rstrip()
                paper, date = line.split(' ')
                dates[paper] = date
                count += 1

        print("{0} dates were found\n".format(count))

        for key,value in dates.items():
            self.papers[key].date = value

     
    def process_titles(self, file):

        print("Reading titles file at {0}".format(file))
        count = 0
        titles = collections.defaultdict(str)

        with open(file) as dates_file:
            for line in dates_file:
                line = line.rstrip()
                paper = line.split(' ')[0]
                title = line.split(' ')[1:]
                titles[paper] = ' '.join(title)
                count += 1

        print("{0} titles were found\n".format(count))

        for key,value in titles.items():
            self.papers[key].title = value

    def process_authors(self, file):

        print("Reading authors file at {0}".format(file))
        count = 0
        authors = collections.defaultdict(str)

        with open(file) as dates_file:
            for line in dates_file:
                line = line.rstrip()
                paper = line.split(' ')[0]
                author = line.split(' ')[1:]
                authors[paper] = '  '.join(author)
                count += 1

        print("{0} authors were found\n".format(count))

        for key,value in authors.items():
            self.papers[key].author = value

    def load_papers(self):
        self.process_citations(Papers.CITATIONS_FILE)
        self.process_dates(Papers.DATES_FILE)
        self.process_titles(Papers.TITLES_FILE)
        self.process_authors(Papers.AUTHORS_FILE)


