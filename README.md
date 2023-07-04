# Event Management and Reservation Web Application
<img width="942" alt="p1" src="https://github.com/SalahEddine-Ghannouch/GetTicket_Events_Django/assets/79339578/241bb844-1c45-4856-a1db-596ec8ec7bee">
<img width="942" alt="p2" src="https://github.com/SalahEddine-Ghannouch/GetTicket_Events_Django/assets/79339578/8d1d02b6-900c-402f-b342-648acdb1a3d3">

This Django project aims to develop a web application for the management and online reservation of events, this project caters to three main actors: the administrator, the organizer, and the customer. Each actor has specific functionalities and access levels within the application.

## Actors and Functionalities

### Administrator

The administrator plays a crucial role in overseeing the entire system. They possess the following capabilities:

- **User Management**: The administrator has the authority to manage user accounts, including creating, modifying, and deleting user profiles. They can handle user roles and permissions to ensure proper access control.

- **Event Management**: The administrator has full control over events on the platform. They can add, modify, and remove events as necessary. Additionally, they are responsible for validating events proposed by organizers to maintain quality standards.

- **Events Dashboard**: The administrator can access a comprehensive dashboard that provides an overview of all events on the platform. This dashboard serves as a monitoring tool, allowing the administrator to track key metrics and gain insights into the system's performance.

### Organizer

Organizers are individuals or entities responsible for planning and executing events. They are granted the following functionalities:

- **Add Events**: Organizers can create and add new events to the platform. They provide detailed information about the event, including its title, description, date, time, location, and any additional relevant details.

- **Event Information**: Organizers have access to view and review all the information related to the events they have proposed. This includes the event details, participant lists, ticket sales, and any updates or modifications.

- **Modify Events**: Organizers can make changes to the events they have created, such as updating event details, rescheduling, or making any necessary adjustments.

- **Event Dashboard**: Organizers are provided with a dedicated dashboard that offers an overview of their events. This dashboard allows organizers to track ticket sales, participant registrations, and other event-related metrics.

### Customer

Customers are the users of the application who are interested in discovering and attending events. They have the following functionalities:

- **Event Exploration**: Customers can browse and explore all events available on the platform. They can view event details, including descriptions, dates, times, locations, categories, and other relevant information.

- **Event Search**: Customers have the ability to search for specific events using keywords, categories, or other search criteria. This allows them to find events that align with their interests.

- **Online Ticket Purchase**: Customers can conveniently purchase event tickets online through the application. They can select the desired number of tickets and complete the purchase securely.

- **Profile Management**: Customers can manage their profiles, including updating personal information, adding a profile picture, and modifying preferences to enhance their overall experience.

- **Reservation Management**: Customers have access to a list of their reservations, which provides an overview of the events they have booked tickets for. They can view reservation details, make changes, or cancel reservations if necessary.

- **Notification Management**: Customers can manage their notification preferences, allowing them to receive relevant updates and reminders about upcoming events, ticket availability, or any changes related to their reservations.

## Installation and Setup

To set up the project locally, please follow these steps:

1. Clone the project repository from [GitHub](https://github.com/SalahEddine-Ghannouch/GetTicket_Events_Django.git).

2. Install the required dependencies by running the command `pip install -r requirements.txt` in your terminal.

4. Apply the database migrations using the command `python manage.py migrate`.

5. Create a superuser account for the administrator.
