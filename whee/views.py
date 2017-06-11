import colander
import deform.widget

from pyramid.view import view_config


class User(colander.MappingSchema):
    first_name = colander.SchemaNode(colander.String())
    last_name = colander.SchemaNode(colander.String())
    email = colander.SchemaNode(colander.Email(msg=None))
    tickets = colander.SchemaNode(colander.Int())


class Users(colander.SequenceSchema):
    user = User()


class Schema(colander.MappingSchema):
    Users = Users()


class RegisterView(object):
    def __init__(self,request):
        self.request = request

    @property
    def register_form(self):
        schema = Schema()
        return deform.Form(schema, buttons=('submit'))

    @property
    def reqts(self):
        return self.register_form.get_widget_resources()

    @view_config(route_name='register_view', renderer='templates/register_view.jinja2')
    def register_view(self):
        form = self.register_form.render()

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.register_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(form=e.render())

        return dict(form=form)
