from mcp.server.fastmcp import FastMCP 
import mysql.connector 
mcp = FastMCP("Student Database")

@mcp.tool()
def get_student_data():
    """Get all student data from MySQL database."""
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=" data_science",
    port=3306
)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM student_info_ai")
    
    rows = cursor.fetchall()
    cursor.close()
    
    return rows
    # if __name__=="__manin__";mcp.run