from flask import Flask, render_template, Response, url_for,request,redirect
import mysql.connector
import smtplib 
app=Flask(__name__)
# Configure MySQL connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='testing'
)

# Configure SMTP email settings
smtp_host = 'smtp.gmail.com'
smtp_port = 465
smtp_username = 'igatajohn15@gmail.com'
smtp_password = 'trailblazer1'
@app.route('/')
def index():
    image_urls=['static/laptop.jpeg','static/pcb.jpg','static/ai.jpg','static/logo.jpg']
    return render_template('index.html',image_urls=image_urls)

@app.route('/about')
def about():
    image_urls=['static/laptop.jpeg','static/pcb.jpg','static/ai.jpg','static/logo.jpg']
    return render_template('about.html',image_urls=image_urls)
@app.route('/product')
def product():
    image_urls=['static/laptop.jpeg','static/pcb.jpg','static/ai.jpg','static/logo.jpg']
    return render_template('product.html',image_urls=image_urls)
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/place_order',methods=['GET','POST'])
def place_order():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        address=request.form['address']
        phone=request.form['phone']
           # Save order details to the database
        cursor = db.cursor()
        query = "INSERT INTO quantum (name, email, address, phone) VALUES (%s, %s, %s, %s)"
        values = (name, email, address, phone)
        cursor.execute(query, values)
        db.commit()
           # Send confirmation email
        sender_email = 'igatajohn15@gmail.com'
        receiver_email = email
        message = f"Dear {name},\n\nThank you for placing your order with us.\n\nWe will process your order and provide further updates soon.\n\nBest regards,\nQuantum Innovative Technologies"
        smtp_server = smtplib.SMTP(smtp_host, smtp_port)
        smtp_server.starttls()
        smtp_server.login(smtp_username, smtp_password)
        smtp_server.sendmail(sender_email, receiver_email, message)
        smtp_server.quit()
        return redirect(url_for('confirmation'),name=name)
    return render_template('place_order.html')
if __name__=='__main__':
    app.run(debug=True)