import theano

class Mixin(object):

    name = None
    priority = 0

    def setup(self, model):
        self.arch = model.arch
        inputs = self.get_inputs()

        self.inputs = []

        for input in inputs:
            if input not in self.inputs:
                self.inputs.append(input)

        self.result = self.get_result()

        self.func = self.create_function()

    def get_result(self):
        raise NotImplementedError

    def get_inputs(self):
        raise NotImplementedError

    def create_function(self):
        return theano.function(self.inputs, self.result,
                               allow_input_downcast=True)


