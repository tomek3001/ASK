using System;
using System.Collections.Generic;
using System.Collections;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Microsoft.Win32;
using System.Diagnostics;


namespace zadanie1
{


    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {



        // Variable to calculate how many characters should be removed from code string
        int new_command_length = 0;

        // Variable for counting lines of assembler code
        uint code_lines = 0;

        // Bool value to check if a new line was recently added to program - if so, enable removing last line
        bool new_command_added = false;

        // Current line counter (step mode)
        int current_step = 0;

        //
        Char[] step_separators = { '\n' };
        Char[] line_separators = { ' ', ','};
        //String[] lines;

        static Dictionary<string, Register> generate_registers()
        {
            Register AX = new Register();
            Register BX = new Register();
            Register CX = new Register();
            Register DX = new Register();
            Register Accum = new Register();
            Dictionary<string, Register> registers = new Dictionary<string, Register>();
            registers.Add("AX", AX);
            registers.Add("BX", BX);
            registers.Add("CX", CX);
            registers.Add("DX", DX);
            registers.Add("Accum", Accum);
            return registers;
        }
        Stack myStack = new Stack();
        private char KeyPress(object sender, System.Windows.Forms.KeyPressEventArgs e)
        {
            return e.KeyChar;
        }

        public Dictionary<string, Register> registers = generate_registers();
        Operations work = new Operations();

        public int interupt_handling(String function, String number)
        {
            DateTime time = DateTime.Now;
            //Na razie argument number nie jest używane ponieważ obsługujemy tylko przerwanie 21 oraz wiele jego funkcji
            switch (function)
            {
                case "0":
                    System.Environment.Exit(0);
                    break;
                case "2A":
                    int year = time.Year;
                    int month = time.Month;
                    int day = time.Day;
                    String dayOfWeek = time.DayOfWeek.ToString().PadLeft(16, '0');
                    string year_string = Convert.ToString(year, 2);
                    var first = year_string.Substring(0, (int)(year_string.Length / 2));
                    var last = year_string.Substring((int)(year_string.Length / 2), (int)(year_string.Length / 2));
                    int val1 = Convert.ToInt32(last, 2);
                    int val2 = Convert.ToInt32(first, 2);
                    registers["AX"].Write(false, val1); //Zapisanie roku
                    registers["AX"].Write(true, val2);

                    registers["DX"].Write(true, month); //Zapisanie miesiąca
                    registers["DX"].Write(false, day);  //Zapisanie dnia
                    break;

                case "2C":
                    int hour = time.Hour;
                    int minute = time.Minute;
                    int second = time.Second;
                    int milisecond = time.Millisecond / 10;
                    registers["CX"].Write(true, hour);
                    registers["CX"].Write(false, minute);
                    registers["DX"].Write(true, second);
                    registers["DX"].Write(false, milisecond);
                    break;
                case "36":
                    DriveInfo cDrive = new DriveInfo("C");
                    if (cDrive.IsReady)
                    {
                        Console.WriteLine("\tFree space:\t{0}",
                            cDrive.AvailableFreeSpace);
                    }
                    break;
                default:
                    break;
            }
            return 0;
        }
        public void execute(string from, string to, string operation)
        {
            switch (operation)
            {
                case "ADD":
                    if (from[0] == '#')
                    {
                        int exception = work.intToRegister(from, registers["Accum"]);
                        if (exception != -1)
                        {
                            exception = work.add(registers["Accum"], registers[to], registers["Accum"]);
                            if (exception == -2)
                            {
                                MessageBox.Show("Sum is too big, operation skipped");
                            }
                            else
                            {
                                work.move(registers["Accum"], registers[to], true, true);
                                work.move(registers["Accum"], registers[to], false, false);
                            }
                        }
                        else
                        {
                            MessageBox.Show("Sum is too big, operation skipped");
                        }
                    }
                    else
                    {
                        int exception = work.add(registers[from], registers[to], registers[to]);
                        if (exception == -2)
                        {
                            MessageBox.Show("Sum is too big, operation skipped");
                        }
                    }
                    break;
                case "SUB":
                    if (from[0] == '#')
                    {
                        work.intToRegister(from, registers["Accum"]);
                        int exception = work.add(registers[to], registers["Accum"], registers[to], false);
                        if (exception == -1)
                        {
                            MessageBox.Show("Our program doesn't support negative numbers, operation skipped");
                        }
                    }
                    else
                    {
                        int exception = work.add(registers[to], registers[from], registers[to], false);
                        if (exception == -1)
                        {
                            MessageBox.Show("Our program doesn't support negative numbers, operation skipped");
                        }
                    }
                    break;
                case "MOV":
                    if (from[0] == '#')
                    {
                        work.intToRegister(from, registers["Accum"]);
                        work.move(registers["Accum"], registers[to], true, true);
                        work.move(registers["Accum"], registers[to], false, false);
                    }
                    else
                    {
                        work.move(registers[from], registers[to], true, true);
                        work.move(registers[from], registers[to], false, false);
                    }
                    break;
                case "PUSH":
                    String name = (from[0] + "X");
                    myStack.Push(registers[name]);
                    break;
                case "POP":
                    myStack.Pop();
                    break;
                case "INT":
                    interupt_handling(from, to);
                    break;
                default:
                    break;
            }
        }

        // Clear all registers
        public void registersReset()
        {

            foreach (var key in registers.Keys)
            {
                registers[key].dataH = 0;
                registers[key].dataL = 0;
                registersUpdate();
            }

        }

        public void registersUpdate()
        {
            this.DataContext = this;
            this.AXVal = work.connetct(registers["AX"]);
            AHValWindow.Text = Convert.ToString(registers["AX"].dataH, 2).PadLeft(8, '0');
            ALValWindow.Text = Convert.ToString(registers["AX"].dataL, 2).PadLeft(8, '0');
            this.BXVal = work.connetct(registers["BX"]);
            BHValWindow.Text = Convert.ToString(registers["BX"].dataH, 2).PadLeft(8, '0');
            BLValWindow.Text = Convert.ToString(registers["BX"].dataL, 2).PadLeft(8, '0');
            this.CXVal = work.connetct(registers["CX"]);
            CHValWindow.Text = Convert.ToString(registers["CX"].dataH, 2).PadLeft(8, '0');
            CLValWindow.Text = Convert.ToString(registers["CX"].dataL, 2).PadLeft(8, '0');
            this.DXVal = work.connetct(registers["DX"]);
            DHValWindow.Text = Convert.ToString(registers["DX"].dataH, 2).PadLeft(8, '0');
            DLValWindow.Text = Convert.ToString(registers["DX"].dataL, 2).PadLeft(8, '0');
        }

        // List of available arguments
        protected static List<String> registerList = new List<String>() {
                                        "AX",
                                        "BX",
                                        "CX",
                                        "DX"
                                        };

        // List of available functions
        protected static List<String> functionList = new List<String>() {
                                        "0",
                                        "2A",
                                        "36",
                                        "2C",
                                        "2",
                                        "1",
                                        "5",
                                        "30",
                                        "2E",
                                        "2D"
                                        };

        public bool isProperRegister(string register)
        {
            foreach (string item in registerList)
            {
                if (item.Equals(register))
                    return true;
            }
            return false;
        }

        public bool isProperFunction(string function)
        {
            foreach (string item in functionList)
            {
                if (item.Equals(function))
                    return true;
            }
            return false;
        }

        // Delay function
        async Task TimeDelay()
        {
            await Task.Delay(50);
        }

        public void PerformAction(string current_action)
        {

            String[] lines = current_action.Split(line_separators, StringSplitOptions.RemoveEmptyEntries);
            string operation = lines[1];
            if (operation == "ADD" | operation == "SUB" | operation == "MOV")
            {
                string from = lines[3];
                string to = lines[2];
                execute(from, to, operation);
                registersUpdate();
            }
            else if (operation == "PUSH" | operation == "POP")
            {
                string register = lines[2];
                if (operation == "PUSH")
                    MessageBox.Show("No to pushowanko z " + register + ".");
                else if (operation == "POP")
                    MessageBox.Show("No to popowanko na " + register + ".");
                execute("", register, operation);
            }
            else if (operation == "INT")
            {
                string function = lines[3];
                string interruption = lines[2];
                execute(function, interruption, operation);
            }
        }

        //*************************************GLOBAL REGISTER VARIABLES**************************************
        public int AXVal
        {
            get { return (int)GetValue(AXValProperty); }
            set { SetValue(AXValProperty, value); }

        }

        public static readonly DependencyProperty AXValProperty =
            DependencyProperty.Register("AXVal", typeof(int), typeof(MainWindow));


        public int BXVal
        {
            get { return (int)GetValue(BXValProperty); }
            set { SetValue(BXValProperty, value); }

        }

        public static readonly DependencyProperty BXValProperty =
            DependencyProperty.Register("BXVal", typeof(int), typeof(MainWindow));

        public int CXVal
        {
            get { return (int)GetValue(CXValProperty); }
            set { SetValue(CXValProperty, value); }

        }

        public static readonly DependencyProperty CXValProperty =
            DependencyProperty.Register("CXVal", typeof(int), typeof(MainWindow));

        public int DXVal
        {
            get { return (int)GetValue(DXValProperty); }
            set { SetValue(DXValProperty, value); }

        }

        public static readonly DependencyProperty DXValProperty =
            DependencyProperty.Register("DXVal", typeof(int), typeof(MainWindow));

        //****************************************************************************************************





        public MainWindow()
        {
            InitializeComponent();
            registersReset();
        }

        private async void RunButton_Click(object sender, RoutedEventArgs e)
        {

            String[] lines = OutputTextBox.Text.Split(step_separators, StringSplitOptions.RemoveEmptyEntries);

            if (lines.Length == 0)
                MessageBox.Show("There is no code to run!");
            else
            {
                for (; current_step < lines.Length; current_step++)
                {
                    CurrStepVal.Text = lines[current_step];
                    PerformAction(CurrStepVal.Text);
                    await TimeDelay();
                }
            MessageBox.Show("Reached the end of the code.");
            }

        }

        private void StepButton_Click(object sender, RoutedEventArgs e)
        {

            String[] lines = OutputTextBox.Text.Split(step_separators, StringSplitOptions.RemoveEmptyEntries);
            if (lines.Length == 0)
                MessageBox.Show("There is no code to run!");
            else
            {
                if (current_step < lines.Length)
                {
                    CurrStepVal.Text = lines[current_step];
                    PerformAction(CurrStepVal.Text);
                    current_step += 1;
                    if (current_step == lines.Length)
                        MessageBox.Show("You have reached the end of the code.");
                }
                else
                    MessageBox.Show("You have already reached the end of the code!");
            }

        }

        // Reset all variables and text boxes
        private void ClearButton_Click(object sender, RoutedEventArgs e)
        {
            OutputTextBox.Text = "";
            code_lines = 0;
            registersReset();
            current_step = 0;
            CurrStepVal.Text = "";
            ARG1Val.Text = "";
            ARG2Val.Text = "";
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            int original_length = OutputTextBox.Text.Length;
            int operation_type = 0;

            // Check which command is selected
            string przycisk = "";
            if (ADDButton.IsChecked == true)
            {
                przycisk = "ADD";
                operation_type = 1;
            } 
            else if (SUBButton.IsChecked == true)
            { 
                przycisk = "SUB";
                operation_type = 1;
            }
            else if (MOVButton.IsChecked == true)
            {
                przycisk = "MOV";
                operation_type = 1;
            } 
            else if (PUSHButton.IsChecked == true)
            {
                przycisk = "PUSH";
                operation_type = 2;
            } 
            else if (POPButton.IsChecked == true)
            {
                przycisk = "POP";
                operation_type = 2;
            } 
            else if (INTButton.IsChecked == true)
            {
                przycisk = "INT";
                operation_type = 3;
            }

            // Add new line of code, validate arguments before adding
            if (operation_type == 1)
            {
                if (ARG1Val.Text == "" | ARG2Val.Text == "")
                    MessageBox.Show("Two arguments required");
                else if (isProperRegister(ARG1Val.Text) == true && (isProperRegister(ARG2Val.Text) == true || (ARG2Val.Text[0] == '#' && uint.TryParse(ARG2Val.Text.TrimStart('#'), out _))))
                {
                    code_lines += 1;
                    OutputTextBox.Text = OutputTextBox.Text + code_lines + ". " + przycisk + " " + ARG1Val.Text + ", " + ARG2Val.Text + "\n";
                    new_command_length = OutputTextBox.Text.Length - original_length;
                    new_command_added = true;
                }
                else
                {
                    ARG1Val.Text = "";
                    ARG2Val.Text = "";
                    MessageBox.Show("Wrong argument!!! Available arguments: " + String.Join(", ", registerList.ToArray()) + 
                        ". If you want to enter an integer, use #<int> formatting (only second argument can be a number).");
                }
            }
            else if (operation_type == 2)
            {
                if (ARG1Val.Text == "" && ARG2Val.Text == "")
                    MessageBox.Show("No argument given.");
                else if (isProperRegister(ARG1Val.Text) == true && ARG2Val.Text == "")
                {
                    code_lines += 1;
                    OutputTextBox.Text = OutputTextBox.Text + code_lines + ". " + przycisk + " " + ARG1Val.Text + "\n";
                    new_command_length = OutputTextBox.Text.Length - original_length;
                    new_command_added = true;
                }
                else if (isProperRegister(ARG1Val.Text) == true && ARG2Val.Text != "")
                    MessageBox.Show("PUSH/PULL require only one argument.");
                else
                {
                    ARG1Val.Text = "";
                    ARG2Val.Text = "";
                    MessageBox.Show("Wrong argument!!! Available arguments: " + String.Join(", ", registerList.ToArray()) + ".");
                }
            }
            else if (operation_type == 3)
            {
                if (ARG1Val.Text == "" | ARG2Val.Text == "")
                    MessageBox.Show("Two arguments required");
                else if (ARG1Val.Text == "21" && isProperFunction(ARG2Val.Text) == true)
                {
                    code_lines += 1;
                    OutputTextBox.Text = OutputTextBox.Text + code_lines + ". " + przycisk + " " + ARG1Val.Text + ", " + ARG2Val.Text + "\n";
                    new_command_length = OutputTextBox.Text.Length - original_length;
                    new_command_added = true;
                }
                else
                {
                    ARG1Val.Text = "";
                    ARG2Val.Text = "";
                    MessageBox.Show("Wrong argument!!! The first arugment is an interruption number and the second argument is a function numer. " +
                        "Available interruptions: 21. Available functions: " + String.Join(", ", functionList.ToArray()) + ".");
                }
            }



        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {

            // Remove newly added line - only if possible
            if (OutputTextBox.Text.Length > 0)
            {
                if (new_command_added)
                {
                    OutputTextBox.Text = OutputTextBox.Text.Remove(OutputTextBox.Text.Length - new_command_length);
                    new_command_added = false;
                    code_lines -= 1;
                }
                else
                    MessageBox.Show("Only the last line can be removed.");
            }
            else
                MessageBox.Show("Command list is empty - nothing to remove.");
        }

        private void SaveButton_Click(object sender, RoutedEventArgs e)
        {
            // Save current 
            string path = "";
            SaveFileDialog sfd = new SaveFileDialog();
            sfd.Filter = "Text files (*.txt)|*.txt";
            Nullable<bool> dialogOK = sfd.ShowDialog();
            if (dialogOK == true)
            {
                path = sfd.FileNames[0];
            }
            if (path != "")
            {
                File.WriteAllText(path, OutputTextBox.Text);
                MessageBox.Show("Succesfully saved.");
            }
            else
                MessageBox.Show("Failed to save.");
        }

        private void LoadButton_Click(object sender, RoutedEventArgs e)
        { 
            // Load saved program
            string path = "";
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Multiselect = false;
            ofd.Filter = "Text files (*.txt)|*.txt";

            Nullable<bool> dialogOK = ofd.ShowDialog();
            if (dialogOK == true)
            {
                path = @ofd.FileNames[0];
            }
            if (path != "")
            {
                code_lines = Convert.ToUInt32(File.ReadLines(path).Count());
                OutputTextBox.Text = File.ReadAllText(path);
                new_command_added = false;
            }
        }

        private void ARG1Val_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void POPButton_Checked(object sender, RoutedEventArgs e)
        {

        }
    }
}