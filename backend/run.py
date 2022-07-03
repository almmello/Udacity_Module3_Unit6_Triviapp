#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

#Importing the app from package
from trivyur import create_app

app = create_app()

# Default port:
if __name__ == '__main__':
    app.run(debug=True)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''