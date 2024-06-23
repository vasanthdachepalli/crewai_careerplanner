from crewai_tools import SerperDevTool,ScrapeWebsiteTool,PDFSearchTool,FileReadTool
scrapewebtool = ScrapeWebsiteTool()
search_tool = SerperDevTool()
scrapespecial = ScrapeWebsiteTool(website_url=['https://www.careers360.com/','https://collegedunia.com/',])


# Initialize the tool allowing for any PDF content search if the path is provided during execution
pdftool = PDFSearchTool()


file_search_tool = FileReadTool(file_path='task_repeation.md')