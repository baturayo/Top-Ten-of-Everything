
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 9637061
#    Student name: Baturay Ofluoglu
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files may be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  The Top Ten of Everything 
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface design to produce a useful
#  application for accessing online data.  See the instruction
#  sheet accompanying this template for full details.
#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
#  Import the modules needed for this assignment.  You may not import
#  any other modules or rely on any other files.  All data and images
#  needed for your solution must be sourced from the Internet.
#

# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import the Tkinter functions
from Tkinter import *

# Import Python's HTML parser
from HTMLParser import *

#Import sqlite3 library
from sqlite3 import*

#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a GIF image, return a Tkinter
#  PhotoImage object suitable for use as the 'image' attribute
#  in a Tkinter Label widget or any other such widget that
#  can display images.
#
def gif_to_PhotoImage(gif_image):

    # Encode the byte stream as a base-64 character string
    # (MIME Base 64 format)
    characters = gif_image.encode('base64', 'strict')

    # Return the result as a Tkinter PhotoImage
    return PhotoImage(data=characters)



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a JPG or PNG image, return a
#  Tkinter PhotoImage object suitable for use as the 'image'
#  attribute in a Tkinter Label widget or any other such widget
#  that can display images.  If positive integers are supplied for
#  the width and height (in pixels) the image will be resized
#  accordingly.
#
def image_to_PhotoImage(image, width = None, height = None):

    # Import the Python Imaging Library, if it exists
    try:
        from PIL import Image, ImageTk
    except:
        raise Exception, 'Python Imaging Library has not been installed properly!'

    # Import StringIO for character conversions
    from StringIO import StringIO

    # Convert the raw bytes into characters
    image_chars = StringIO(image)

    # Open the character string as a PIL image, if possible
    try:
        pil_image = Image.open(image_chars)
    except:
        raise Exception, 'Cannot recognise image given to "image_to_Photoimage" function\n' + \
                         'Confirm that image was downloaded correctly'
    
    # Resize the image, if a new size has been provided
    if type(width) == int and type(height) == int and width > 0 and height > 0:
        pil_image = pil_image.resize((width, height), Image.ANTIALIAS)

    # Return the result as a Tkinter PhotoImage
    return ImageTk.PhotoImage(pil_image)



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by putting your solution below.
#
##### DEVELOP YOUR SOLUTION HERE #####
# download all URL images
def download_URLS():
    global byte_top10image, byte_spotify_image, byte_nba_image, byte_book_image


    ##################IMAGE URL###################
    #-----------------MainPage URL--------------_#

    mainpage_url = 'https://www.chatteryak.com/wp-content/uploads/2015/04/top-10.jpg'
    # Read the contents of the web page as a string
    byte_top10image = urlopen(mainpage_url).read()

    #---------------- Spotify URL----------------#
    spotify_url = 'http://d2c87l0yth4zbw.global.ssl.fastly.net/i/_global/open-graph-default.png'
    # Read the contents of the web page as a string
    byte_spotify_image = urlopen(spotify_url).read()

    #---------------- UK Cinema URL--------------------#
    cinema_url = 'https://metrouk2.files.wordpress.com/2016/01/2361.jpg'
    # Read the contents of the web page as a string
    byte_nba_image = urlopen(cinema_url).read()

    #---------------- Book URL--------------------#
    book_url = 'http://hdwallpaperbackgrounds.net/wp-content/uploads/2015/10/Book-Art-Typography-Wallpaper.jpg'

    # Read the contents of the web page as a string
    byte_book_image = urlopen(book_url).read()

# Return HTML code of any URL
def download_HTML_code(url):
    return urlopen(url).read()


# Create Pop-up windows by taking window title, byte image,top10 data URL and top10 data variables
def topLevelWindow(title, byte_image, data_url, top10list):
    # which_top10_clicked indicates which button is clicked 0=non clicked 1= spotify 2= UK Cinema 3= book
    global which_top10_clicked
    # Create pop-up window
    window = Toplevel()

    # Give the popup window a title
    window.title(title)

    # Convert image to PhotoImage
    image = image_to_PhotoImage(byte_image, width=600, height=400)

    # Create label contains Image
    top10image_label = Label(window, image=image)

    # Add label to pop-up window
    top10image_label.pack()

    # Generate an empty String that stores top10 List Data
    string=""

    # Create interface for spotify contains each element in Spotify Top10 List
    if data_url == spotify_url:
        for index in range(9):
            #update string
            string = string + str("("+str(index+1)+")  -"+top10list[index]+"\n")
        string = string + str("("+str(10)+")-"+top10list[9]+"\n")

        #Create Label
        l = Label(window, justify=LEFT, text=string, font=('Helvetica', 15, 'italic'), fg="darkgreen")

        #Add Label To Window
        l.pack(anchor=W)

        #Update which_top10_clicked status
        which_top10_clicked = 1

        #Update save button status to normal
        save['state'] = 'normal'

    # Create interface for UK cinemas contains each element in UK Cinemas Top10 List
    elif data_url == uk_cinemas_url:
        for index in range(10):
            string = string + str("["+str(index+1)+"] "+top10list[index]+"\n")
        l = Label(window, borderwidth=6, relief=GROOVE, text=string, font=('Times New Roman',13, 'bold'), fg ="darkred")
        l.pack()
        which_top10_clicked = 2
        save['state'] = 'normal'

    # Create interface for Book contains each element in game Top10 List
    elif data_url == book_url:
        for index in range(10):
            string = string + str(index+1)+" - "+top10list[index]+"\n"
            string = string.upper()
        l = Label(window, width=54, borderwidth=4, relief=SUNKEN, text=string, font=('Tahoma', 18, 'bold'), fg="White", bg="Black")
        l.pack()
        which_top10_clicked = 3
        save['state'] = 'normal'

    # Adding URL page at the bottom of pop-up page where the top10 data stored
    urllabel = Label(window, text=data_url)
    urllabel.pack()

    # Start the event loop
    window.mainloop()

# Taking Top10 data from downloaded HTML code by using regular expressions
def top10(url, regex):
    #Download html code of web page
    html_code = download_HTML_code(url)

    #Find relevant data stored in html code
    _top10_ = findall(regex, html_code)

    #create a list that stores unicode string data
    top10_unescaped = []
    h = HTMLParser()
    #Index of list
    counter = 0
    for index in _top10_:
        counter= counter + 1

        top10_unescaped.append(h.unescape(index))
        #Dont take more than 10 elements to array
        if counter == 10:
            break
    #return top10 data list
    return top10_unescaped

# Create first page interface when the programs open
def mainpage():

    #Define global save button to reach that button from another methods
    global save

    #Download all images via URL
    download_URLS()

    # Create main menu window
    window = Tk()

    # Give the window a title
    window.title('The Top Ten of Everything')

    # Convert image to PhotoImage
    top10image = image_to_PhotoImage(byte_top10image, width=600, height=400)

    # Create label contains Image
    top10image_label = Label(window, image=top10image)

    # Create label contains String
    string_label = Label(window, text="Choose from the Top Ten...")

    # Create save button
    save = Button(window, command=lambda: sql_connection(),
                   text="Save Latest Selection", state=DISABLED)

    # Create a button which shows the top10 list when pressed
    spotify = Button(window,command=lambda: topLevelWindow(spotify_title, byte_spotify_image, spotify_url,
                                                           top10(spotify_url,regex_spotify)),
                     text='Spotify')
    film = Button(window,command=lambda: topLevelWindow(film_title, byte_nba_image,uk_cinemas_url,
                                                        top10(uk_cinemas_url,regex_uk_cinema)),
                  text="UK Cinemas")
    game = Button(window,command=lambda: topLevelWindow(book_title, byte_book_image,book_url ,
                                                        top10(book_url,regex_book)),
                  text="Books")




    # Add labels and buttons to window
    top10image_label.pack()
    string_label.pack(padx=5)
    save.pack(ipadx=200)
    spotify.pack(padx=5, ipadx=50, side=LEFT)
    film.pack(padx=5, ipadx=50, side=LEFT)
    game.pack(padx=5, ipadx=50, side=LEFT)

    # Start the event loop
    window.mainloop()

def sql_connection():
    # Connect to data base that is created before and located at the same path with this .py code
    connection = connect('top_ten.db')
    top10_db = connection.cursor()

    # Drop the initiated table when connect to sql db
    top10_db.execute("DROP TABLE Top_Ten")

    # Recreate db each times when program opens with two columns
    top10_db.execute('''CREATE TABLE Top_Ten
             ('Rank' INTEGER, 'Description' TEXT)''')

    # If spotify clicked call spotify top10 list
    if which_top10_clicked == 1:
        top10list = top10(spotify_url, regex_spotify)
    # If UK Cinema clicked call UK Cinema top10 list
    elif which_top10_clicked == 2:
        top10list = top10(uk_cinemas_url, regex_uk_cinema)
    # If Book clicked call Book top10 list
    elif which_top10_clicked == 3:
        top10list = top10(book_url, regex_book)

    # Insert a row of data with two dimension.
    # First dimension stores rank and second stores top 10 list
    list_top10 = []
    for x in range(10):
        row = []
        string = (top10list[x])

        for y in range(1):
            row.append(x+1)
            row.append(string)
        list_top10.append(row)

    # Create a template includes SQL codes to transfer list_top10 to sqlite
    template = "INSERT INTO Top_Ten VALUES (?,?)"
    connection.executemany(template,list_top10)

    # Save (connection) the changes
    connection.commit()

    # Close the cursor and release the server connection.
    top10_db.close()
    connection.close()

################################---Main Program----#############################################

#0 = Not Clicked ;1 = spotify ; 2 = film; 3 = book
which_top10_clicked = 0

# Title of windows
spotify_title = "Daily Top 10 Hits on Spotify"
film_title = "Top 10 films on UK Cinema"
book_title = "Top 10 Book Names"

# Top 10 data URL's
spotify_url = "https://open.spotify.com/user/spotify/playlist/5FJXhjdILmRA2z5bvz4nzf"
book_url = "https://www.dymocks.com.au/top-101"
uk_cinemas_url = "http://www.launchingfilms.com/research-databank/current-top-15-films"

# Regular Expressions for each top10 data
regex_spotify = "><span class=\"track-name\">(.*?)</span>"
regex_uk_cinema = "<h5>(.*?)</h5>"
regex_book = "/\">(.*?)</a></strong><br />"

mainpage()

################################---------#############################################