# Covid Tracker
A web app for storing data about covid patients

## [Usage]()

## Installation Instruction
To get the code..
1. Cloning the repository:
  ```bash
  git clone https://github.com/benjaminbills/covid-tracker.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd covid-tracker
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
3. Migrate the application
  ```bash
  python3 manage.py makemigrations && migrate
  ```
4. Running the application
  ```bash
  python3 manage.py runserver
  ```

Open the application on your browser `https//localhost:8000`.

### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request

### Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/benjaminbills/covid-tracker/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/benjaminbills/covid-tracker/issues/new). Please include sample queries and their corresponding results.

### Contributors
[Benjamin Obafemi](https://github.com/benjaminbills)



## Technologies Used.

- [Python](https://www.python.org/)- version 3.8.5.
- [Bootstrap](https://getbootstrap.com/)- version 5.0
- [Django](https://www.djangoproject.com/) - version 3.2
- [Check requirements for more details](https://github.com/benjaminbills/covid-tracker/blob/master/requirements.txt)

## Contact Information
If you have any enquiries you can reach out to us on the following emails
1. obafemibenjamins@gmail.com


### Copyright and License
[MIT License](https://github.com/benjaminbills/covid-tracker/blob/master/License)
