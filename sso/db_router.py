class SSORouter:
	"""
	auth와 contenttypes 앱의 모델에 일어나는 DB operation에 대한 라우터이다.
	"""
	route_app_labels = {'sso', 'auth', 'contenttypes', 'admin', 'sessions'}
	db_name = 'sso_db'

	def db_for_read(self, model, **hints):
			"""
			Attempts to read auth and contenttypes models go to sso_db.
			"""
			if model._meta.app_label in self.route_app_labels:
					return self.db_name
			return None

	def db_for_write(self, model, **hints):
			"""
			Attempts to write auth and contenttypes models go to sso_db.
			"""
			if model._meta.app_label in self.route_app_labels:
					return self.db_name
			return None

	def allow_relation(self, obj1, obj2, **hints):
			"""
			Allow relations if a model in the auth or contenttypes apps is
			involved.
			"""
			if (
					obj1._meta.app_label in self.route_app_labels or
					obj2._meta.app_label in self.route_app_labels
			):
					return True
			return None

	def allow_migrate(self, db, app_label, model_name=None, **hints):
			"""
			Make sure the auth and contenttypes apps only appear in the
			'sso_db' database.
			"""
			if app_label in self.route_app_labels:
					return db == self.db_name
			return None