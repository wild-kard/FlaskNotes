from website import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
    #turn this off for production build, automatically reruns application