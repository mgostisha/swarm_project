from django.db import models

# Create your models here.
class SimulationParameters(models.Model):

	# Unit labels for help text
	units = {
		'coord': 'kpc',
		'vel': 'km/s',
		'col_density': 'log particles/cm^2',
		'density': 'log particles/cm^3',
		'time': 'Gyr',
		'mass': 'log Msun',
		'unitless': ''
	}

	# ----------------------------------------
	# ---------- INITIAL CONDITIONS ----------
	# ----------------------------------------

	# Fields for initial coordinates
	x_coord = models.FloatField(default=0.0, help_text=units['coord'])
	y_coord = models.FloatField(default=-8.0, help_text=units['coord'])
	z_coord = models.FloatField(default=0.0, help_text=units['coord'])

	# Fields for initial velocities
	vx_vel = models.FloatField(default=220.0, help_text=units['vel'])
	vy_vel = models.FloatField(default=0.0, help_text=units['vel'])
	vz_vel = models.FloatField(default=0.0, help_text=units['vel'])

	# Field for column density of particles
	column_density = models.FloatField(default=20.0, help_text=units['col_density'])

	# Fields for standard deviations for use with picking particles form Gaussian distribution
	sigma_coord = models.FloatField(default=0.1, help_text=units['coord'])
	sigma_vel = models.FloatField(default=0.1, help_text=units['vel'])
	sigma_col_den = models.FloatField(default=1.0, help_text=units['col_density'])

	# -----------------------------------------
	# ------------ DRAG PARAMETERS ------------
	# -----------------------------------------

	# True/False field for turning on drag
	drag_option = models.BooleanField(default=False)

	# Options for the drag velocity field
	vel_options = (
		('ZV', 'Zero Velocity'),
		('MP', 'Match Potential'),
		('RO', 'Radial Outflow')
	)

	# Field for choosing the velocity model in the simulation. The choices are above
	# and the form will handle whether or not any additional input field need ot be shown
	# or not. Only the Radial Outflow model needs further input from the user. The max
	# length of 2 just ensures that only one of the two letter abbreviations is valid.
	vel_field = models.CharField(max_length=2, default='ZV', choices=vel_options)

	# Additional Velocity fields, Radial Outflow (RO)
	RO_initial_vel = models.FloatField(default=0.0, help_text=units['vel'])
	RO_r_scale = models.FloatField(default=0.0, help_text=units['coord'])

	# Options for the drag density field
	den_options = (
		('CD', 'Constant Density'),
		('PL', 'Power Law'),
		('DD', 'Density Disks')
	)

	# Field for choosing the density model in the simulation. The choices are above
	# and the form will decide which fields should be shown. All density options require
	# additional input from the user. The max length of two just ensures that only one of
	# the two letter abbreviations is valid.
	den_field = models.CharField(max_length=2, default='CD', choices=den_options)

	# Additional Density field parameters, Constant Density (CD)
	CD_density = models.FloatField(default=-3.0, help_text=units['density'])

	# Additional Density field parameters, Power Law (PL)
	PL_density = models.FloatField(default=-3.0, help_text=units['density'])
	PL_r_scale = models.FloatField(default=0.0, help_text=units['coord'])
	PL_alpha_exp = models.FloatField(default=0.0, help_text=units['unitless'])

	# Additional Density field parameters, Density Disks (DD)
	DD_density1 = models.FloatField(default=0.0, help_text=units['density'])
	DD_density2 = models.FloatField(default=0.0, help_text=units['density'])
	DD_density3 = models.FloatField(default=0.0, help_text=units['density'])

	DD_r_scale1 = models.FloatField(default=0.0, help_text=units['coord'])
	DD_r_scale2 = models.FloatField(default=0.0, help_text=units['coord'])
	DD_r_scale3 = models.FloatField(default=0.0, help_text=units['coord'])

	DD_z_scale1 = models.FloatField(default=0.0, help_text=units['coord'])
	DD_z_scale2 = models.FloatField(default=0.0, help_text=units['coord'])
	DD_z_scale3 = models.FloatField(default=0.0, help_text=units['coord'])

	# Function to handle whether extra inputs are needed for radial outflow velocity option
	def is_radial_outflow(self):
		return self.vel_field == 'RO'

	# Three functions to handle which extra input options should be shown for the density field
	def is_constant_density(self):
		return self.den_field == 'CD'

	def is_power_law(self):
		return self.den_field == 'PL'

	def is_density_disks(self):
		return self.den_field == 'DD'

	# -------------------------------------------
	# ---------- SIMULATION PARAMETERS ----------
	# -------------------------------------------

	# Options for the gravitation potential used in the simulation
	potential_choices = (
		('PS', 'Point Source'),
		('WF', 'Wolfire')
	)

	# Field for choosing the potential to use. Max length of 2 ensures that only our two letter
	# abbreviations are valid. The both the point source and the Wolfire option require additional
	# user input which will be handled by the form and the boolean functions below
	potential = models.CharField(max_length=2, default='WF', choices=potential_choices)

	# Additional fields for point source gravitational potential
	PS_mass = models.FloatField(default=4.0, help_text=units['mass'])

	# Additional fields for the Wolfire gravitational potential
	WF_disk = models.BooleanField(default=True)
	WF_bulge = models.BooleanField(default=True)
	WF_halo = models.BooleanField(default=True)

	# Field for total time and number of timesteps
	total_time = models.FloatField(default=1.0, help_text=units['time'])
	timesteps = models.IntegerField(default=1000, help_text=units['unitless'])

	# Field for the number of particles to be simulated
	n_particles = models.IntegerField(default=5, help_text=units['unitless'])

	# Field for the Integrator Convergence Tolerance
	int_con_tol = models.FloatField(default=-3.0, help_text="log pc")

	# Field for the user's email address
	email_address = models.EmailField()

	# Functions to help the form decide which extra inputs to display
	def is_point_source(self):
		return self.potential == 'PS'

	def is_wolfire(self):
		return self.potential == 'WF'

	# Override __unicode__ to print a nicer string
	def __unicode__(self):
		return "Email: {0}, Coords: <{1}, {2}, {3}>, Drag: {4}, Potential: {5}".format(
			self.email_address, self.x_coord, self.y_coord, self.z_coord, self.drag_option, self.potential
		)
