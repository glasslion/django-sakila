# Builtin Models

### Actor

The `Actor` model contains information for all actors.

**Relations**: The `FilmActor` model has Foreignkey to the `Actor` model

**Fields**:

- `actor_id`:primary key 
- `first_name`: The actor's first name.
- `last_name`: The actor's last name.
- `last_update`: The time that the object was created or most recently updated.


### Adderss

The `Adderss` model contains address information for customers, staff, and stores.

**Relations**: The `Customer`, `Staff` and `Store` models have Foreignkey to the `Adderss` model


**Fields**:

- `address_id`: The primary key
- `address`: The first line of an address.
- `address2`: An optional second line of an address.
- `district`: The region of an address, this may be a state, province, prefecture, etc.
- `city`: A foreign key pointing to the City model.
- `postal_code`: The postal code or ZIP code of the address (where applicable).
- `phone`: The telephone number for the address.
- `last_update`: The time that the object was created or most recently updated.


### Category
The `Category` model lists the categories that can be assigned to a film.

**Relations**: The `Category` model and the `Film` model are associated with the `ManyToManyField` through the `FilmCategory` model.

**Fields**:

- `category_id`: The primary key
- `name`: The name of the category
- `last_update`: The time that the object was created or most recently updated.

### City

The `City` model table contains a list of cities.

Relations The `City` model has Foreignkey to the `Country` model. The `Address` model has Foreignkey to the `City` model.

**Fields**:

 - `city_id`: The primary key
 - `city`: The name of the city.
 - `country_id`: A foreign key identifying the country that the city belongs to.
 - `last_update`: The time that the object was created or most recently updated.

### Country

The `Country` model table contains a list of countries.

Relations The `City` model has Foreignkey to the `Country` model. 

**Fields**:

- `country_id`: The primary key
- `country`: The name of the country.
- `last_update`: The time that the object was created or most recently updated.


### Customer

The `Customer` model contains information of all customers.

**Relations**: The `Customer` model has Foreignkey to the `Address` and `Store` models. The `Payment` and ` Rental` models have Foreignkey to the `Customer` model.

**Fields**:

- `customer_id`: The primary key
- `store_id`: A foreign key identifying the customer's “home store.” Customers are not limited to renting only from this store, but this is the store they generally shop at.
- `first_name`: The customer's first name.
- `last_name`: The customer's last name.
- `email`: The customer's email address.
- `address`: A foreign key identifying the customer's address.
- `active`: Indicates whether the customer is an active customer. Setting this to FALSE serves as an alternative to deleting a customer outright.
- `create_date`: The date the customer was added to the system.
- `last_update`: The time that the object was created or most recently updated.


### Film
The `Film` model represents films potentially in stock in the stores. The actual in-stock copies of each film are represented in the `Inventory` model.

**Relations**: The `Film` model has Foreignkey to the `Language` model. The `Inventory` model has Foreignkey to the `Film` model. The `Film` model is associated with the `Category` and `Actor` model through the `FilmCategory` and `FilmActor` individually.

**Fields**:

- `film_id`: The primary key
- `title`: The title of the film.
- `description`: A short description or plot summary of the film.
- `release_year`: The year in which the movie was released.
- `language`: A foreign key identifies the language of the film.
- `original_language`: A foreign key identifies the original language of the film. Used when a film has been dubbed into a new language.
- `rental_duration`: The length of the rental period, in days.
- `rental_rate`: The cost to rent the film for the period specified in the `rental_duration` field.
- `length`: The duration of the film, in minutes.
- `replacement_cost`: The amount charged to the customer if the film is not returned or is returned in a damaged state.
- `rating`: The rating assigned to the film. Can be one of: G, PG, PG-13, R, or NC-17.
- `special_features`: Lists which common special features are included on the DVD. Can be zero or more of: Trailers, Commentaries, Deleted Scenes, Behind the Scenes.
- `last_update`: The time that the object was created or most recently updated.


### FilmActor
The `FilmActor` model is used to support a many-to-many relationship between the `Film` model and the `Actor` model. For each actor in a given film, there will be one `FilmActor` object listing the actor and film.

**Relations**: The `FilmActor` model has Foreignkey to the `Film` and `Actor` models.

**Fields**:
- `actor_id`: A foreign key identifying the actor.
- `film_id`: A foreign key identifying the film.
- `last_update`: The time that the object was created or most recently updated.


### FilmCategory

The `FilmCategory` model is used to support a many-to-many relationship between the `Film` model and the `Category` model. For each category applied to a film, there will be one `FilmCategory` object listing the category and film.

**Relations**: The `FilmCategory` model has Foreignkey to the `Film` and `Category` models.

**Fields**:

- `film_id`: A foreign key identifying the film.
- `category_id`: A foreign key identifying the category.
- `last_update`: The time that the object was created or most recently updated

### Inventory

Each `Inventory` object represents a copy of a given film in a given store.

**Relations**: The `Inventory` model has Foreignkey to the `Film` and `Category` models. The `Rental` model has Foreignkey to the `Inventory` model.

**Fields**:

- `inventory_id`: The primary key
- `film`: A foreign key pointing to the film this item represents.
- `stord`: A foreign key pointing to the store stocking this item.
- `last_update`: The time that the object was created or most recently updated.

### Language

The `Language` model stores the possible languages that films can have for their language and original language values.

**Relations**: The `Film` model has Foreignkey to the `Language` model.

**Fields**:

- `language_id`: The primary key
- `name`: The English name of the language.
- `last_update`: The time that the object was created or most recently updated.



### Payment

Each `Payment` object represents a payment made by a customer, with information such as the amount and the rental being paid for (when applicable).

**Relations**: The `Payment` model has Foreignkey to the `Customer`, `Rental` and `Staff` models.

**Fields**:

- `payment_id`: The primary key
- `customer`: A foreign key identifying the customer whose balance the payment is being applied to.
- `staff`: A foreign key identifying the staff member who processed the payment.
- `rental`: A foreign key identifying the rental that the payment is being applied to. This is optional because some payments are for outstanding fees and may not be directly related to a rental.
- `amount`: The amount of the payment.
- `payment_date`: The date the payment was processed.
- `last_update`: The time that the object was created or most recently updated.


### Rental

Each `Rental` object represents each rental of each inventory item with information about who rented what item, when it was rented, and when it was returned.

**Relations**: The `Rental` model has Foreignkey to the `Inventory`, `Customer`, and `Staff` models. The `Payment` model has Foreignkey to the `Rental` model.

**Fields**:

- `rental_id`: The primary key
- `rental_date`: The date and time that the item was rented.
- `inventory`: The item being rented.
- `customer`: The customer renting the item.
- `return_date`: The date and time the item was returned.
- `staff`: The staff member who processed the rental.
- `last_update`: The time that the object was created or most recently updated.


### Staff

The `Staff` model lists all staff members, including information on email address, login information, and picture.

**Relations**: The `Staff` model has Foreignkey to the `Store` and `Address` models. The `Rental`, `Payment` and `Store` models have Foreignkey to the `Staff` model.

**Fields**:

- `staff_id`: The primary key
- `first_name`: The first name of the staff member.
- `last_name`: The last name of the staff member.
- `address`: A foreign key to the staff member's address.
- `picture`: A BLOB containing a photograph of the employee.
- `email`: The staff member's email address.
- `store`: The staff member's “home store”. The employee can work at other stores but is generally assigned to the store listed.
- `active`: Whether this is an active employee. If employees leave their record are not deleted from the database, instead this field is set to FALSE.
- `username`: The user name used by the staff member to access the rental system.
- `password`: The password used by the staff member to access the rental system. The password should be stored as a hash using the SHA1() function.
- `last_update`: The time that the object was created or most recently updated.

### Store

The `Store` model lists all stores in the system. All inventory is assigned to specific stores, and staff and customers are assigned a “home store”.

**Relations**: The `Store` model has Foreignkey to the `Staff` and `Address` models. The `Staff`, `Custom` and `Inventory` models have Foreignkey to the `Store` model.

**Fields**:
- `store_id`: The primary key
- `manager_staff_id`: A foreign key identifying the manager of this store.
- `address_`: A foreign key identifying the address of this store.
- `last_update`: The time that the object was created or most recently updated.
