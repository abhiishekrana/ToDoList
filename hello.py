import mysql.connector

connection=mysql.connector.connect(host="database-1.cxiqoa7uqghb.ap-south-1.rds.amazonaws.com", user="admin", password="password123",database="db0")

def updatestatus(decodeBody,connection):
  print("Received insert request")
  cursor = connection.cursor()
  team_id=decodeBody["team_id"]
  member_id=decodeBody["member_id"]

    
  sql="""SELECT EXISTS(SELECT * FROM team_member WHERE team_id = %s)"""
  cursor.execute(sql,(id,))
  extracted_data = cursor.fetchone()
  
  if extracted_data[0]!=0:
    sql = """UPDATE team_members SET status="accepted" where status="pending" and team_id=%s and member_id=%s"""
    val = (team_id,member_id)
    cursor.execute(sql, val)
    connection.commit()
    
    response_data={'message':'status updated successfully'}
    return utils.response("Passed",response_data)
  else :  
    cursor.close()
    response_data={'message':'this team doesnt exists'}
    
    #return http response 
    return utils.response("Failed",response_data)

  

