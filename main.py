from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import main_calorie

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriePage(MethodView):
    def get(self):
        calorie_form = CalorieForm()
        return render_template('calorie_page.html', calorieform=calorie_form)


class ResultsPage(MethodView):
    def post(self):
        calorieform = CalorieForm(request.form)
        user1 = main_calorie.User(calorieform.weight.data, calorieform.height.data, calorieform.age.data)
        temp1 = main_calorie.Temperature(calorieform.city.data, calorieform.country.data)
        cal = main_calorie.Calorie(calorieform.city.data, calorieform.country.data,
                                   float(calorieform.weight.data), float(calorieform.height.data), float(calorieform.age.data))

        return render_template('results.html', calorie_count=cal.calculate())


class CalorieForm(Form):
    weight = StringField("Weight:")
    height = StringField("Height:")
    age = StringField("Age:")
    city = StringField("City:")
    country = StringField("Country:")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie_form', view_func=CaloriePage.as_view('calorie_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))
app.run(debug=True)
