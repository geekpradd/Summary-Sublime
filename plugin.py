import sublime, sublime_plugin
try:
    from .summary import SummaryTool
except:
    from summary import SummaryTool

class summaryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            region_text = self.view.substr(region)
            if not region_text is "":
                summarized_text = self.get_summary(region_text)
                self.view.replace(edit, region, summarized_text)
                summary_ratio = "Summary Ratio: %s" % (100 - (100 * (len(summarized_text) / (len(region_text)))))
                self.view.set_status("summary","Summary Ratio: %s" % summary_ratio)
            else:
                self.view.set_status("summary", "Summary Error: No text has been selected ")

    def get_summary(self, text):           
        st = SummaryTool()
        content = text
        sentences_dic = st.get_senteces_ranks(content)

        summary = st.get_summary(None, content, sentences_dic)

        return summary
    