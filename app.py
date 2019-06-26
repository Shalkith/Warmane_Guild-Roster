from flask import Flask, render_template, request
from data import Articles
from data import Warmane
import string
app = Flask(__name__)
app.debug=True

Articles = Articles()


class BenefitTemplateService(object):

    @staticmethod
    def create(params):
        # some validation here

        params['credit_behavior'] = "none"
        return params


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return '404'
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return '500'
    return render_template('404.html'), 404


@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        parameters = request.form.to_dict()
        response = BenefitTemplateService.create(parameters)
        print(response['Guild'])
        try:
            return render_template('warmane.html', data = Warmane(string.capwords(response['Guild']),response['Realm']), result = response)
        except:
            return render_template('warmane.html', data = Warmane("Born+On+A+Blood+Moon","Lordaeron"))

    else:
        return render_template('warmane.html', data = Warmane("Born+On+A+Blood+Moon","Lordaeron"))

@app.route('/about')
def about():
    return render_template('about.html')

#@app.route('/warmane')
#def warmane():
#    return render_template('warmane.html', data = Warmane())
    #return render_template('warmane.html', data = Warmane(), name = Guildname())


@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)


if __name__ == '__main__':
    #Guildname()
    app.run(host='0.0.0.0')
