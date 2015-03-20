from django.shortcuts import render
from django.core.validators import EmailValidator, validate_email
from django.core.exceptions import ValidationError

from swarm.forms import SimulationParameterForm

# Index View
# This is the main landing page for swarm
def index(request):
	context_dict = {'boldmessage': "This is the NEW swarm."}
	return render(request, 'swarm/index.html', context_dict)


# About View
# This view tells a little bit about the simulation
def about(request):
	return render(request, 'swarm/about.html', {})


# Submit Job View
# This view allows the user to submit a job to be run
def submit_job(request):
	# Is the request an HTTP POST?
	if request.method == 'POST':
		# If so, try and process the form
		form = SimulationParameterForm(request.POST)

		# Save the form to the database if everything is valid
		if form.is_valid:
			# Special email validator
			if validate_email_address(request.POST['email_address']):
				form.save(commit=True)

				# Return the user to a job submission success page
				return success(request)
		else:
			# Print the errors if the form wasn't valid
			print form.errors
	else:
		# Produce an empty form to return to the user in the case of a GET request
		form = SimulationParameterForm()

	# Render the page and print the errors (if applicable) in the case of a bad
	# form or a GET request
	return render(request, 'swarm/submit-job.html', {'form': form})


def validate_email_address(email):
	try:
		validate_email(email)
		return True
	except ValidationError:
		return False



def success(request):
	return render(request, 'swarm/success.html', {})


def details(request):
	return render(request, 'swarm/details.html', {})


def documentation(request):
	return render(request, 'swarm/docs.html', {})
