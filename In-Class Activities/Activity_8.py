import Web_Scraping as wb

def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    main_tree = wb.get_web_tree("https://www.wvu.edu")
    #print(main_tree.xpath)
    # Find any tag with the id wvu-main, then go down one level, and obtain whatever text there is.
    # Right-click on your browser and hit Inspect (Chrome is preferable)
    #uni_name = main_tree.xpath('//*[@id="wvu-main"]/h1/text()')
    #print(uni_name)
    # Let us see how many divs are they under this section
    #all_divs = main_tree.xpath('//*[@id="wvu-main"]/div')
    # This will display the number of sections
    #print(str(len(all_divs)))
    # Interact with the first div

    #first_div = all_divs[0]
    # This will get the number of sections (divs) under the first div.
    #print(str(len(first_div)))
    # This will extract the FIND YOUR VIBE statement from the website.

    be_your_guide = main_tree.xpath('/html/body/main/div[3]/div/div[1]/h2/text()')
    print(be_your_guide)

    future_students = main_tree.xpath('/html/body/main/div[3]/div/div[3]/div[1]/div/h3/text()')
    print(future_students)

    future_students_p = main_tree.xpath('/html/body/main/div[3]/div/div[3]/div[1]/div/p/text()')
    print(future_students_p)

    button = main_tree.xpath('/html/body/main/div[3]/div/div[3]/div[1]/div/a/text()')
    print(button)

    admitted_students = main_tree.xpath('/html/body/main/div[3]/div/div[3]/div[2]/div/h3/text()')
    print(admitted_students)

if __name__ == "__main__":
    main()