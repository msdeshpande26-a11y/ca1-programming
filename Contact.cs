using System;

namespace ContactBookApp
{
    public abstract class ContactBase
    {
        public abstract void DisplayContact();
    }

    public class Contact : ContactBase
    {
        private string mobileNumber;

        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Company { get; set; }
        public string Email { get; set; }
        public DateTime Birthdate { get; set; }

        public string MobileNumber
        {
            get => mobileNumber;
            set
            {
                if (IsValidMobile(value))
                    mobileNumber = value;
                else
                    throw new ArgumentException("Mobile number must be a non-zero, 9-digit positive number.");
            }
        }

        public Contact() { }

        public Contact(string firstName, string lastName, string company,
                       string mobileNumber, string email, DateTime birthdate)
        {
            FirstName = firstName;
            LastName = lastName;
            Company = company;
            MobileNumber = mobileNumber;
            Email = email;
            Birthdate = birthdate;
        }

        public override void DisplayContact()
        {
            Console.WriteLine($"\nContact Details:");
            Console.WriteLine($"Name: {FirstName} {LastName}");
            Console.WriteLine($"Company: {Company}");
            Console.WriteLine($"Mobile: {MobileNumber}");
            Console.WriteLine($"Email: {Email}");
            Console.WriteLine($"Birthdate: {Birthdate:dd MMM yyyy}");
        }

        private bool IsValidMobile(string number)
        {
            return number?.Length == 9 && long.TryParse(number, out long n) && n > 0;
        }
    }
}
