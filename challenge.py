import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "admin123",
  database = "challenge"
)

mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS challenge (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL UNIQUE,
  ISBN VARCHAR(255) NOT NULL UNIQUE
)
""")
print("Table created successfully!")

# function to add a Book
def add_book(mycursor, mydb):
  try:
      sql = "INSERT INTO challenge (title, author, ISBN) VALUES (%s, %s, %s)"
      
      title = input("Enter Title: ")
      author = input("Enter Author: ")
      ISBN = input("Enter isbn: ")
      
      val = (title, author, ISBN)
      
      mycursor.execute(sql, val)
      mydb.commit()
      
      return (mycursor.rowcount, "record(s) inserted.")
  except mysql.connector.Error as e:
    print(f"Error: {e}")
    return 0

  finally:
        # Example of closing (you would do this at the end of your app)
        if 'mydb' in locals() and mydb.is_connected():
            mycursor.close()
            mydb.close()
        pass
add_book(mycursor,mydb)

def search_book():
  try:
    book_author = input("Enter the book author: ")
    sql = "SELECT title FROM challenge WHERE author = %s"
    val = (book_author, )
    
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    
    if myresult:
      print(f"Book Title: {myresult[0]}")
    
    else:
      print(f"No book found for author: {book_author}")
    
  except mysql.connector.Error as e:
    print(f"Error: {e}")
    return 0

  finally:
        # Example of closing (you would do this at the end of your app)
        if 'mydb' in locals() and mydb.is_connected():
            mycursor.close()
            mydb.close()
        pass
      
search_book()
    
  
def get_book(mycursor):
  
  try:
      sql = ("SELECT * FROM challenge")
      mycursor.execute(sql)
      myresult = mycursor.fetchall()
      
      
      if not myresult:
        print("No books found.")
        return
      
      print("\n--- All Books in Table ---")
      header = f"{'ID':<5} | {'Title':<30} | {'Author':<25} | {'ISBN':<15}"
      print(header)
      print("-" * len(header))
      
      for row in myresult:
        # row is a tuple: (id, title, author, ISBN)
        print(f"{row[0]:<5} | {row[1]:<30} | {row[2]:<25} | {row[3]:<15}")
        
      print("-" * len(header))  # Print a footer line
      print(f"Total books found: {len(myresult)}\n")
  except mysql.connector.Error as e:
        print(f"Error fetching books: {e}")
        
  finally:
        # Example of closing (you would do this at the end of your app)
      if 'mydb' in locals() and mydb.is_connected():
           mycursor.close()
           mydb.close()
      pass     
        
get_book(mycursor)


def delete_book(mycursor):
  try:
    book_id = int(input("Enter the book ID to delete: "))
    sql = ("DELETE FROM challenge WHERE id = %s")
    val= (book_id,)
    getbook_id = ("SELECT id FROM challenge")
    
    mycursor.execute(sql, val)
    mydb.commit()
    
    if mycursor.rowcount > 0:
      print(f"The book with {book_id} book ID has been deleted successfully!")
    else:
      print(f"There's no book in the system with this {book_id} book ID! No Records were deleted. please try again")
      
    
    
    
  except ValueError:
        # This catches errors if the user types 'abc' instead of a number
        print(f"Error: '{book_id}' is not a valid ID. Please enter a number.")
  except mysql.connector.Error as e:
        print(f"Database Error: {e}")
        
  finally:
        # Example of closing (you would do this at the end of your app)
      if 'mydb' in locals() and mydb.is_connected():
           mycursor.close()
           mydb.close()
      pass  
  
delete_book(mycursor)
  