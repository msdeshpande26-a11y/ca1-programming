using System;

namespace ContactBookApp
{
    class Program
    {
        static void Main(string[] args)
        {
            ContactBook contactBook = new ContactBook();

            // Preload 20 contacts (9-digit mobiles)
            contactBook.AddContact(new Contact("Emily", "Blackwell", "Dublin Business School", "087111111", "emily.blackwell@dbs.ie", new DateTime(1990, 1, 1)));
            contactBook.AddContact(new Contact("James", "O'Connor", "Google Ireland", "087111112", "james.oconnor@google.com", new DateTime(1988, 5, 12)));
            contactBook.AddContact(new Contact("Sarah", "Murphy", "Microsoft Dublin", "087111113", "sarah.murphy@microsoft.com", new DateTime(1992, 3, 8)));
            contactBook.AddContact(new Contact("Michael", "Kelly", "Accenture", "087111114", "michael.kelly@accenture.com", new DateTime(1985, 7, 20)));
            contactBook.AddContact(new Contact("Laura", "Byrne", "Meta Ireland", "087111115", "laura.byrne@meta.com", new DateTime(1991, 11, 2)));
            contactBook.AddContact(new Contact("Patrick", "Walsh", "Amazon Dublin", "087111116", "patrick.walsh@amazon.com", new DateTime(1989, 9, 15)));
            contactBook.AddContact(new Contact("Aoife", "Ryan", "Deloitte", "087111117", "aoife.ryan@deloitte.ie", new DateTime(1993, 6, 25)));
            contactBook.AddContact(new Contact("Conor", "Smith", "PwC Ireland", "087111118", "conor.smith@pwc.ie", new DateTime(1987, 4, 10)));
            contactBook.AddContact(new Contact("Niamh", "Fitzgerald", "EY Ireland", "087111119", "niamh.fitzgerald@ey.com", new DateTime(1990, 12, 30)));
            contactBook.AddContact(new Contact("Sean", "Doyle", "KPMG Ireland", "087111120", "sean.doyle@kpmg.ie", new DateTime(1986, 2, 18)));
            contactBook.AddContact(new Contact("Ciara", "Gallagher", "LinkedIn Dublin", "087111121", "ciara.gallagher@linkedin.com", new DateTime(1994, 8, 5)));
            contactBook.AddContact(new Contact("Brian", "Hughes", "Stripe Dublin", "087111122", "brian.hughes@stripe.com", new DateTime(1989, 10, 22)));
            contactBook.AddContact(new Contact("Kate", "O'Brien", "HubSpot Dublin", "087111123", "kate.obrien@hubspot.com", new DateTime(1992, 1, 14)));
            contactBook.AddContact(new Contact("Daniel", "Moore", "Dropbox Dublin", "087111124", "daniel.moore@dropbox.com", new DateTime(1988, 3, 27)));
            contactBook.AddContact(new Contact("Emma", "Clarke", "Twitter Dublin", "087111125", "emma.clarke@twitter.com", new DateTime(1991, 5, 9)));
            contactBook.AddContact(new Contact("Luke", "Murray", "Salesforce Dublin", "087111126", "luke.murray@salesforce.com", new DateTime(1987, 7, 19)));
            contactBook.AddContact(new Contact("Rebecca", "Kavanagh", "Oracle Dublin", "087111127", "rebecca.kavanagh@oracle.com", new DateTime(1993, 9, 3)));
            contactBook.AddContact(new Contact("Thomas", "Flynn", "SAP Ireland", "087111128", "thomas.flynn@sap.com", new DateTime(1985, 11, 11)));
            contactBook.AddContact(new Contact("Megan", "Roche", "IBM Dublin", "087111129", "megan.roche@ibm.com", new DateTime(1990, 6, 7)));
            contactBook.AddContact(new Contact("David", "O'Sullivan", "Intel Ireland", "087111130", "david.osullivan@intel.com", new DateTime(1986, 4, 21)));

            int choice;
            do
            {
                Console.WriteLine("\n--- Contact Book Menu ---");
                Console.WriteLine("1: Add Contact");
                Console.WriteLine("2: Show All Contacts");
                Console.WriteLine("3: Show Contact Details (by Name)");
                Console.WriteLine("4: Update Contact (by Name)");
                Console.WriteLine("5: Delete Contact (by Mobile)");
                Console.WriteLine("0: Exit");
                Console.Write("Enter your choice: ");

                bool valid = int.TryParse(Console.ReadLine(), out choice);
                if (!valid)
                {
                    Console.WriteLine("Invalid input. Please enter a number.");
                    continue;
                }

                switch (choice)
                {
                    case 1:
                        try
                        {
                            Console.Write("First Name: ");
                            string fname = Console.ReadLine();
                            Console.Write("Last Name: ");
                            string lname = Console.ReadLine();
                            Console.Write("Company: ");
                            string company = Console.ReadLine();
                            Console.Write("Mobile Number (9 digits): ");
                            string mobile = Console.ReadLine();
                            Console.Write("Email: ");
                            string email = Console.ReadLine();
                            Console.Write("Birthdate (yyyy-mm-dd): ");
                            string bdInput = Console.ReadLine();
                            if (!DateTime.TryParse(bdInput, out DateTime birthdate))
                            {
                                Console.WriteLine("Invalid birthdate format.");
                                break;
                            }

                            Contact newContact = new Contact(fname, lname, company, mobile, email, birthdate);
                            contactBook.AddContact(newContact);
                        }
                        catch (Exception ex)
                        {
                            Console.WriteLine($"Error: {ex.Message}");
                        }
                        break;

                    case 2:
                        contactBook.ShowAllContacts();
                        break;

                    case 3:
                        Console.Write("Enter First Name: ");
                        string searchFirst = Console.ReadLine();
                        Console.Write("Enter Last Name: ");
                        string searchLast = Console.ReadLine();
                        contactBook.ShowContactDetailsByName(searchFirst, searchLast);
                        break;

                    case 4:
                        Console.Write("Enter First Name: ");
                        string updateFirst = Console.ReadLine();
                        Console.Write("Enter Last Name: ");
                        string updateLast = Console.ReadLine();
                        Console.Write("Enter New Email: ");
                        string updatedEmail = Console.ReadLine();
                        contactBook.UpdateContactByName(updateFirst, updateLast, updatedEmail);
                        break;

                    case 5:
                        Console.Write("Enter Mobile Number: ");
                        string deleteMobile = Console.ReadLine();
                        contactBook.DeleteContact(deleteMobile);
                        break;

                    case 0:
                        Console.WriteLine("Exiting Contact Book. Goodbye!");
                        break;

                    default:
                        Console.WriteLine("Invalid choice. Try again.");
                        break;
                }
            } while (choice != 0);
        }
    }
}
