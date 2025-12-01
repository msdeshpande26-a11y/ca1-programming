using System;

public class MainClass
{
    public static void Main(string[] args)
    {
        ExtensionAssistant assistant = new ExtensionAssistant();

        Console.WriteLine("=== File Extension Assistant (Abstract OOP Version) ===");
        Console.WriteLine("Enter a file extension (e.g., mp4, jpg, pdf). Type 'exit' to quit.");

        while (true)
        {
            Console.Write("\nYour query: ");
            string input = Console.ReadLine()?.Trim();

            if (string.Equals(input, "exit", StringComparison.OrdinalIgnoreCase))
            {
                Console.WriteLine("Goodbye! Thanks for using the File Extension Assistant.");
                break;
            }

            assistant.QueryExtension(input);
        }
    }
}
