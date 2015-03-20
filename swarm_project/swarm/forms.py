from django import forms
from swarm.models import SimulationParameters


class SimulationParameterForm(forms.ModelForm):

	# ---------------------------------
	# ---------- COORDINATES ----------
	# ---------------------------------

	# Minimum and maximum values for validation
	xy_min = -25.0
	xy_max = 25.0
	z_min = -10.0
	z_max = 10.0

	# Custom error messages for coordinate entry errors
	coord_error_messages = {
		'required': 'You must enter a coordinate value.',
		'invalid': 'Your entry is invalid. Please enter a valid coordinate.',
		'min_value': 'Your coordinate value is too low.',
		'max_value': 'Your coordinate value is too high'
	}

	# x, y, and z coordinate fields
	x_coord = forms.FloatField(
		max_value=xy_max,
		min_value=xy_min,
		error_messages=coord_error_messages,
		initial=0.0,
		help_text="x coordinate (kpc): ")

	y_coord = forms.FloatField(
		max_value=xy_max,
		min_value=xy_min,
		error_messages=coord_error_messages,
		initial=-8.0,
		help_text="y coordinate (kpc): ")

	z_coord = forms.FloatField(
		max_value=z_max,
		min_value=z_min,
		error_messages=coord_error_messages,
		initial=0.0,
		help_text="z coordinate (kpc): ")

	# --------------------------------
	# ---------- VELOCITIES ----------
	# --------------------------------

	# Velocity minimum and maximum values for validation
	vel_min = -5000.0
	vel_max = 5000.0

	# Custom error messages for velocity entry errors
	vel_error_messages = {
		'required': 'You must enter a velocity value.',
		'invalid': 'Your entry is invalid. Please enter a valid velocity value.',
		'min_value': 'Your velocity value is too low.',
		'max_value': 'Your velocity value is too high'
	}

	# x, y, and z velocity form fields
	vx_vel = forms.FloatField(
		max_value=vel_max,
		min_value=vel_min,
		error_messages=vel_error_messages,
		initial=220.0,
		help_text="x velocity (km/s) ")

	vy_vel = forms.FloatField(
		max_value=vel_max,
		min_value=vel_min,
		error_messages=vel_error_messages,
		initial=0.0,
		help_text="y velocity (km/s): ")

	vz_vel = forms.FloatField(
		max_value=vel_max,
		min_value=vel_min,
		error_messages=vel_error_messages,
		initial=0.0,
		help_text="z velocity (km/s): ")

	# ------------------------------------
	# ---------- COLUMN DENSITY ----------
	# ------------------------------------

	# Minimum and maximum values for column density for validation
	col_den_min = -30.0
	col_den_max = 30.0

	# Custom error messages for column density values
	col_den_error_messages = {
		'required': 'You must enter a column density value.',
		'invalid': 'Your entry is invalid. Please enter a valid column density value.',
		'min_value': 'Your column density value is too low.',
		'max_value': 'Your column density value is too high'
	}

	# Column density form field
	column_density = forms.FloatField(
		max_value=col_den_max,
		min_value=col_den_min,
		error_messages=col_den_error_messages,
		initial=20.0,
		help_text="Column density (log particles/cm^2): ")

	# ----------------------------------
	# ---------- SIGMA VALUES ----------
	# ----------------------------------

	# Minimum and Maximum sigma values for validation
	sigma_min = -1000.0
	sigma_max = 1000.0

	# Custom error messages for the sigma values
	sigma_error_messages = {
		'required': 'You must enter a sigma value.',
		'invalid': 'Your entry is invalid. Please enter a valid sigma value.',
		'min_value': 'Your sigma value is too low.',
		'max_value': 'Your sigma value is too high'
	}

	# Coordinate, velocity and column density sigma form fields
	sigma_coord = forms.FloatField(
		max_value=sigma_max,
		min_value=sigma_min,
		error_messages=sigma_error_messages,
		initial=0.1,
		help_text="Std. Dev. for coordinates (kpc): ")

	sigma_vel = forms.FloatField(
		max_value=sigma_max,
		min_value=sigma_min,
		error_messages=sigma_error_messages,
		initial=0.1,
		help_text="Std. Dev. for velocities (km/s): ")

	sigma_col_den = forms.FloatField(
		max_value=sigma_max,
		min_value=sigma_min,
		error_messages=sigma_error_messages,
		initial=1.0,
		help_text="Std. Dev. for column density (log particles/cm^2): ")

	# ---------------------------------
	# ---------- DRAG FIELDS ----------
	# ---------------------------------

	# Minimum and maximum parameters for validation
	scale_rad_min = 0.0
	scale_rad_max = 25.0
	scale_z_min = 0.0
	scale_z_max = 10.0
	density_min = -10.0
	density_max = 20.0
	alpha_min = -5.0
	alpha_max = 5.0

	# Options for drag velocity fields
	velocity_options = (
		('ZV', 'Zero Velocity'),
		('MP', 'Match Potential'),
		('RO', 'Radial Outflow')
	)

	# Options for drag density fields
	density_options = (
		('CD', 'Constant Density'),
		('PL', 'Power Law'),
		('DD', 'Density Disks')
	)

	# Custom Velocity Field error messages
	vel_field_error_messages = {
		'required': 'Please choose a velocity field.',
		'invalid_choice': 'Your choice of velocity field is invalid.'
	}

	# Custom Density Field error messages
	den_field_error_messages = {
		'required': 'Please choose a density field.',
		'invalid_choice': 'Your choice of density field is invalid.'
	}

	# Drag option form field, can be either true or false
	drag_option = forms.BooleanField(
		required=False,
		help_text="Drag? ",
		initial=True)

	# Drag Velocity form field
	vel_field = forms.ChoiceField(
		choices=velocity_options,
		error_messages=vel_field_error_messages,
		initial='ZV',
		help_text="Drag Velocity Field: ")

	# Radial Outflow Velocity Field form fields
	RO_r_scale = forms.FloatField(
		max_value=scale_rad_max,
		min_value=scale_rad_min,
		initial=0.0,
		help_text="Radial Outflow Scale Radius (kpc): ")

	RO_initial_vel = forms.FloatField(
		max_value=vel_max,
		min_value=vel_min,
		initial=0.0,
		help_text="Radial Outflow Initial Velocity (km/s): ")

	# Drag Density Field form field
	den_field = forms.ChoiceField(
		choices=density_options,
		error_messages=den_field_error_messages,
		initial='CD',
		help_text="Drag Density Field: ")

	# Additional density field parameter form fields, Constant Density (CD)
	CD_density = forms.FloatField(
		max_value=density_max,
		min_value=density_min,
		initial=-3.0,
		help_text="Constant Density: Central Density (log particles/cm^3): ")

	# Additional density field parameter form fields, Power Law (PL)
	PL_density = forms.FloatField(
		max_value=density_max,
		min_value=density_min,
		initial=-3.0,
		help_text="Power Law: Central Density (log particles/cm^3): ")

	PL_r_scale = forms.FloatField(
		max_value=scale_rad_max,
		min_value=scale_rad_min,
		initial=0.0,
		help_text="Power Law: Scale Radius (kpc): ")

	PL_alpha_exp = forms.FloatField(
		max_value=alpha_max,
		min_value=alpha_min,
		initial=0.0,
		help_text="Power Law: Alpha Exponent: ")

	# Additional density field parameter form fields, Density Disks (DD)
	DD_density1 = forms.FloatField(
		max_value=density_max,
		min_value=density_min,
		initial=0.0,
		help_text="Density Disk 1: Central Density (log particles/cm^3): ")

	DD_density2 = forms.FloatField(
		max_value=density_max,
		min_value=density_min,
		initial=0.0,
		help_text="Density Disk 2: Central Density (log particles/cm^3): ")

	DD_density3 = forms.FloatField(
		max_value=density_max,
		min_value=density_min,
		initial=0.0,
		help_text="Density Disk 3: Central Density (log particles/cm^3): ")

	DD_r_scale1 = forms.FloatField(
		max_value=scale_rad_max,
		min_value=scale_rad_min,
		initial=0.0,
		help_text="Density Disk 1: Scale Radius (kpc): ")

	DD_r_scale2 = forms.FloatField(
		max_value=scale_rad_max,
		min_value=scale_rad_min,
		initial=0.0,
		help_text="Density Disk 2: Scale Radius (kpc): ")

	DD_r_scale3 = forms.FloatField(
		max_value=scale_rad_max,
		min_value=scale_rad_min,
		initial=0.0,
		help_text="Density Disk 3: Scale Radius (kpc): ")

	DD_z_scale1 = forms.FloatField(
		max_value=scale_z_max,
		min_value=scale_z_min,
		initial=0.0,
		help_text="Density Disk 1: Scale Height (kpc): ")

	DD_z_scale2 = forms.FloatField(
		max_value=scale_z_max,
		min_value=scale_z_min,
		initial=0.0,
		help_text="Density Disk 2: Scale Height (kpc): ")

	DD_z_scale3 = forms.FloatField(
		max_value=scale_z_max,
		min_value=scale_z_min,
		initial=0.0,
		help_text="Density Disk 3: Scale Height (kpc): ")

	# ---------------------------------------------
	# ---------- GRAVITATIONAL POTENTIAL ----------
	# ---------------------------------------------

	# Minimum and Maximum values for potential form fields
	ps_mass_min = 0.0
	ps_mass_max = 15.0

	# Custom error messages for potential choice field
	potential_error_messages = {
		'required': 'Please choose a density field.',
		'invalid_choice': 'Your choice of density field is invalid.'
	}

	# Custom error messages for the point source mass form field
	ps_mass_error_messages = {
		'required': 'You must enter a point source mass value.',
		'invalid': 'Your entry is invalid. Please enter a valid point source mass value.',
		'min_value': 'Your point source mass value is too low.',
		'max_value': 'Your point source mass value is too high'
	}

	# Options for gravitational potential
	potential_choices = (
		('PS', 'Point Source'),
		('WF', 'Wolfire')
	)

	# Gravitational potential form field
	potential = forms.ChoiceField(
		choices=potential_choices,
		error_messages=potential_error_messages,
		initial='WF',
		help_text="Gravitational Potential: ")

	# Point source mass form field
	PS_mass = forms.FloatField(
		max_value=ps_mass_max,
		min_value=ps_mass_min,
		error_messages=ps_mass_error_messages,
		initial=0.0,
		help_text="Point Source Mass (log Msun): ")

	# Wolfire component switch fields
	WF_disk = forms.BooleanField(
		required=False,
		initial=True,
		help_text="Wolfire Disk: ")

	WF_bulge = forms.BooleanField(
		required=False,
		initial=True,
		help_text="Wolfire Bulge: ")

	WF_halo = forms.BooleanField(
		required=False,
		initial=True,
		help_text="Wolfire Halo: ")

	# --------------------------------------
	# ---------- TIME INFORMATION ----------
	# --------------------------------------

	# Minimum and Maximum values for the time information
	time_min = 0.1
	time_max = 10.0
	timesteps_min = 100
	timesteps_max = 10000

	# Custom error messages for the time fields
	time_error_messages = {
		'required': 'You must enter a time value.',
		'invalid': 'Your entry is invalid. Please enter a valid time value.',
		'min_value': 'Your time value is too low.',
		'max_value': 'Your time value is too high'
	}

	timestep_error_messages = {
		'required': 'You must enter a timestep value',
		'invalid': 'Your entry is invalid. Please enter a valid timestep value.',
		'min_value': 'Your timestep value is too low.',
		'max_value': 'Your timestep value is too high.'
	}

	# Total time form field
	total_time = forms.FloatField(
		max_value=time_max,
		min_value=time_min,
		error_messages=time_error_messages,
		initial=1.0,
		help_text="Total Time (Gyr): ")

	# Number of timesteps form field
	timesteps = forms.IntegerField(
		max_value=timesteps_max,
		min_value=timesteps_min,
		error_messages=timestep_error_messages,
		initial=1000,
		help_text="Number of Timesteps: ")

	# -------------------------------------------------------------------
	# ---------- PARTICLE AND INTEGRATOR CONVERGENCE TOLERANCE ----------
	# -------------------------------------------------------------------

	# Minimum and maximum values for number of particles in the integrator convergence tolerance
	n_min = 1
	n_max = 10000
	ict_min = -9.0
	ict_max = 0.0

	# Custom error messages for the ICT and number of particles
	ict_error_messages = {
		'required': 'You must enter an ICT value.',
		'invalid': 'Your entry is invalid. Please enter a valid ICT value.',
		'min_value': 'Your ICT value is too low.',
		'max_value': 'Your ICT value is too high'
	}

	n_error_messages = {
		'required': 'You must enter a number of particles value.',
		'invalid': 'Your entry is invalid. Please enter a valid value for the number of particles.',
		'min_value': 'Your number of particles is too low.',
		'max_value': 'Your number of particles is too high'
	}

	# Number of particles form field
	n_particles = forms.IntegerField(
		max_value=n_max,
		min_value=n_min,
		error_messages=n_error_messages,
		initial=5,
		help_text="Number of Particles: ")

	#ICT form field
	int_con_tol = forms.FloatField(
		max_value=ict_max,
		min_value=ict_min,
		error_messages=ict_error_messages,
		initial=-3.0,
		help_text="Integrator Convergence Tolerance (log pc): ")

	# -----------------------------------
	# ---------- EMAIL ADDRESS ----------
	# -----------------------------------

	# Custom errors for the email field
	email_error_messages = {
		'required': 'You must enter your email address.',
		'invalid': 'Your entry is invalid. Please enter a valid email address.'
	}

	# Email address form field
	email_address = forms.EmailField(
		max_length=75,
		error_messages=email_error_messages,
		help_text="Email Address: ")

	class Meta:
		# Link this form with the SimulationParameter Model
		model = SimulationParameters

		# You have to explicitly tell django which fields to either include or exclude.
		# Since we want to include all the fields, we just define an empty exclude variable,
		# thereby implicitly including all the fields
		exclude = ()