# coding=UTF-8
from __future__ import division
import re

# This is a naive text summarization algorithm
# Created by Shlomi Babluki
# April, 2013


class SummaryTool(object):

    # Naive method for splitting a text into sentences
    def split_content_to_sentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")

    # Naive method for splitting a text into paragraphs
    def split_content_to_paragraphs(self, content):
        return content.split("\n\n")

    # Caculate the intersection between 2 sentences
    def sentences_intersection(self, sent1, sent2):

        # split the sentence into words/tokens
        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))

        # If there is not intersection, just return 0
        if (len(s1) + len(s2)) == 0:
            return 0

        # We normalize the result by the average number of words
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)

    # Format a sentence - remove all non-alphbetic chars from the sentence
    # We'll use the formatted sentence as a key in our sentences dictionary
    def format_sentence(self, sentence):
        sentence = re.sub(r'\W+', '', sentence)
        return sentence

    # Convert the content into a dictionary <K, V>
    # k = The formatted sentence
    # V = The rank of the sentence
    def get_senteces_ranks(self, content):

        # Split the content into sentences
        sentences = self.split_content_to_sentences(content)

        # Calculate the intersection of every two sentences
        n = len(sentences)
        values = [[0 for x in range(n)] for x in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])

        # Build the sentences dictionary
        # The score of a sentences is the sum of all its intersection
        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.format_sentence(sentences[i])] = score
        return sentences_dic

    # Return the best sentence in a paragraph
    def get_best_sentence(self, paragraph, sentences_dic):

        # Split the paragraph into sentences
        sentences = self.split_content_to_sentences(paragraph)

        # Ignore short paragraphs
        if len(sentences) < 2:
            return ""

        # Get the best sentence according to the sentences dictionary
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s

        return best_sentence

    # Build the summary
    def get_summary(self, title, content, sentences_dic):

        # Split the content into paragraphs
        paragraphs = self.split_content_to_paragraphs(content)

        # Add the title
        summary = []
        if not title is None:
            summary.append(title.strip())
            summary.append("")

        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)

        return ("\n").join(summary)


# Main method, just run "python summary_tool.py"
def main():

    # Demo
    # Content from: "http://thenextweb.com/apps/2013/03/21/swayy-discover-curate-content/"

    title = """
    Swayy is a beautiful new dashboard for discovering and curating online content [Invites]
    """

    content = """
    Lior Degani, the Co-Founder and head of Marketing of Swayy, pinged me last week when I was in California to tell me about his startup and give me beta access. I heard his pitch and was skeptical. I was also tired, cranky and missing my kids â€“ so my frame of mind wasnâ€™t the most positive.

    I went into Swayy to check it out, and when it asked for access to my Twitter and permission to tweet from my account, all I could think was, â€œIf this thing spams my Twitter account I am going to bitch-slap him all over the Internet.â€ Fortunately that thought stayed in my head, and not out of my mouth.

    One week later, Iâ€™m totally addicted to Swayy and glad I said nothing about the spam (it doesnâ€™t send out spam tweets but I liked the line too much to not use it for this article). I pinged Lior on Facebook with a request for a beta access code for TNW readers. I also asked how soon can I write about it. Itâ€™s that good. Seriously. I use every content curation service online. It really is That Good.

    What is Swayy? Itâ€™s like Percolate and LinkedIn recommended articles, mixed with trending keywords for the topics you find interesting, combined with an analytics dashboard that shows the trends of what you do and how people react to it. I like it for the simplicity and accuracy of the content curation. Everything Iâ€™m actually interested in reading is in one place â€“ I donâ€™t have to skip from another major tech blog over to Harvard Business Review then hop over to another major tech or business blog. Itâ€™s all in there. And it has saved me So Much Time



    After I decided that I trusted the service, I added my Facebook and LinkedIn accounts. The content just got That Much Better. I can share from the service itself, but I generally prefer reading the actual post first â€“ so I end up sharing it from the main link, using Swayy more as a service for discovery.

    Iâ€™m also finding myself checking out trending keywords more often (more often than never, which is how often I do it on Twitter.com).



    The analytics side isnâ€™t as interesting for me right now, but that could be due to the fact that Iâ€™ve barely been online since I came back from the US last weekend. The graphs also havenâ€™t given me any particularly special insights as I canâ€™t see which post got the actual feedback on the graph side (however there are numbers on the Timeline side.) This is a Beta though, and new features are being added and improved daily. Iâ€™m sure this is on the list. As they say, if you arenâ€™t launching with something youâ€™re embarrassed by, youâ€™ve waited too long to launch.

    It was the suggested content that impressed me the most. The articles really are spot on â€“ which is why I pinged Lior again to ask a few questions:

    How do you choose the articles listed on the site? Is there an algorithm involved? And is there any IP?

    Yes, weâ€™re in the process of filing a patent for it. But basically the system works with a Natural Language Processing Engine. Actually, there are several parts for the content matching, but besides analyzing what topics the articles are talking about, we have machine learning algorithms that match you to the relevant suggested stuff. For example, if you shared an article about Zuck that got a good reaction from your followers, we might offer you another one about Kevin Systrom (just a simple example).

    Who came up with the idea for Swayy, and why? And whatâ€™s your business model?

    Our business model is a subscription model for extra social accounts (extra Facebook / Twitter, etc) and team collaboration.

    The idea was born from our day-to-day need to be active on social media, look for the best content to share with our followers, grow them, and measure what content works best.

    Who is on the team?

    Ohad Frankfurt is the CEO, Shlomi Babluki is the CTO and Oz Katz does Product and Engineering, and I [Lior Degani] do Marketing. The four of us are the founders. Oz and I were in 8200 [an elite Israeli army unit] together. Emily Engelson does Community Management and Graphic Design.

    If you use Percolate or read LinkedInâ€™s recommended posts I think youâ€™ll love Swayy.

    âž¤ Want to try Swayy out without having to wait? Go to this secret URL and enter the promotion code thenextweb . The first 300 people to use the code will get access.

    Image credit: Thinkstock

    """

    # Create a SummaryTool object
    st = SummaryTool()

    # Build the sentences dictionary
    sentences_dic = st.get_senteces_ranks(content)

    # Build the summary with the sentences dictionary
    summary = st.get_summary(title, content, sentences_dic)

    # Print the summary
    print (summary)

    # Print the ratio between the summary length and the original length
    print ("")
    print ("Original Length %s" % (len(title) + len(content)))
    print( "Summary Length %s" % len(summary))
    print ("Summary Ratio: %s" % (100 - (100 * (len(summary) / (len(title) + len(content))))))


if __name__ == '__main__':
    main()