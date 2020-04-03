using System;
using System.Collections.Generic;
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

        int new_command_length = 0;

        bool new_command_added = false;

        public void registersReset()
        {

            this.DataContext = this;
            this.AXVal = 0;
            this.AHVal = 0;
            this.ALVal = 0;
            this.BXVal = 0;
            this.BHVal = 0;
            this.BLVal = 0;
            this.CXVal = 0;
            this.CHVal = 0;
            this.CLVal = 0;
            this.DXVal = 0;
            this.DHVal = 0;
            this.DLVal = 0;
        }

        protected static List<String> registerList = new List<String>() {
                                        "AX",
                                        "BX",
                                        "CX",
                                        "DX"
                                        };

        public bool isProperRegister(string register)
        {
            foreach (string item in registerList)
            {
                if (item.Contains(register))
                    return true;
            }
            return false;
        }

        //*************************************GLOBAL REGISTER VARIABLES**************************************
        public int AXVal
        {
            get { return (int)GetValue(AXValProperty); }
            set { SetValue(AXValProperty, value); }

        }

        public static readonly DependencyProperty AXValProperty =
            DependencyProperty.Register("AXVal", typeof(int), typeof(MainWindow));

        public int AHVal
        {
            get { return (int)GetValue(AHValProperty); }
            set { SetValue(AHValProperty, value); }

        }

        public static readonly DependencyProperty AHValProperty =
            DependencyProperty.Register("AHVal", typeof(int), typeof(MainWindow));


        public int ALVal
        {
            get { return (int)GetValue(ALValProperty); }
            set { SetValue(ALValProperty, value); }

        }

        public static readonly DependencyProperty ALValProperty =
            DependencyProperty.Register("ALVal", typeof(int), typeof(MainWindow));


        public int BXVal
        {
            get { return (int)GetValue(BXValProperty); }
            set { SetValue(BXValProperty, value); }

        }

        public static readonly DependencyProperty BXValProperty =
            DependencyProperty.Register("BXVal", typeof(int), typeof(MainWindow));

        public int BHVal
        {
            get { return (int)GetValue(BHValProperty); }
            set { SetValue(BHValProperty, value); }

        }

        public static readonly DependencyProperty BHValProperty =
            DependencyProperty.Register("BHVal", typeof(int), typeof(MainWindow));

        public int BLVal
        {
            get { return (int)GetValue(BLValProperty); }
            set { SetValue(BLValProperty, value); }

        }

        public static readonly DependencyProperty BLValProperty =
            DependencyProperty.Register("BLVal", typeof(int), typeof(MainWindow));

        public int CXVal
        {
            get { return (int)GetValue(CXValProperty); }
            set { SetValue(CXValProperty, value); }

        }

        public static readonly DependencyProperty CXValProperty =
            DependencyProperty.Register("CXVal", typeof(int), typeof(MainWindow));

        public int CHVal
        {
            get { return (int)GetValue(CHValProperty); }
            set { SetValue(CHValProperty, value); }

        }

        public static readonly DependencyProperty CHValProperty =
            DependencyProperty.Register("CHVal", typeof(int), typeof(MainWindow));

        public int CLVal
        {
            get { return (int)GetValue(CLValProperty); }
            set { SetValue(CLValProperty, value); }

        }

        public static readonly DependencyProperty CLValProperty =
            DependencyProperty.Register("CLVal", typeof(int), typeof(MainWindow));

        public int DXVal
        {
            get { return (int)GetValue(DXValProperty); }
            set { SetValue(DXValProperty, value); }

        }

        public static readonly DependencyProperty DXValProperty =
            DependencyProperty.Register("DXVal", typeof(int), typeof(MainWindow));

        public int DHVal
        {
            get { return (int)GetValue(DHValProperty); }
            set { SetValue(DHValProperty, value); }

        }

        public static readonly DependencyProperty DHValProperty =
            DependencyProperty.Register("DHVal", typeof(int), typeof(MainWindow));

        public int DLVal
        {
            get { return (int)GetValue(DLValProperty); }
            set { SetValue(DLValProperty, value); }

        }

        public static readonly DependencyProperty DLValProperty =
            DependencyProperty.Register("DLVal", typeof(int), typeof(MainWindow));

        //****************************************************************************************************





        public MainWindow()
        {
            InitializeComponent();
            registersReset();
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void RunButton_Click(object sender, RoutedEventArgs e)
        {
            string przycisk = "";
            if (ADDButton.IsChecked == true)
                przycisk = "ADD";
            else if (SUBButton.IsChecked == true)
                przycisk = "SUB";
            else if (MOVButton.IsChecked == true)
                przycisk = "MOV";
            
            OutputTextBox.Text = "Wciśnięty został przycisk RUN, a wybrana operacja to " + przycisk +
                ", podczas gdy argument pierwszy to " + ARG1Val.Text + ", a argument drugi to " + ARG2Val.Text + ".";
        }

        private void StepButton_Click(object sender, RoutedEventArgs e)
        {
            string przycisk = "";
            if (ADDButton.IsChecked == true)
                przycisk = "ADD";
            else if (SUBButton.IsChecked == true)
                przycisk = "SUB";
            else if (MOVButton.IsChecked == true)
                przycisk = "MOV";
            OutputTextBox.Text = "Wciśnięty został przycisk STEP, a wybrana operacja to " + przycisk + 
                ", podczas gdy argument pierwszy to " + ARG1Val.Text + ", a argument drugi to " + ARG2Val.Text + ".";
        }

        private void ClearButton_Click(object sender, RoutedEventArgs e)
        {
            OutputTextBox.Text = "";
            registersReset();
        }

        private void ComboBox_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {

        }

        private void Button_Click(object sender, RoutedEventArgs e)
        { 
            int original_length = OutputTextBox.Text.Length;
            string przycisk = "";
            if (ADDButton.IsChecked == true)
                przycisk = "ADD";
            else if (SUBButton.IsChecked == true)
                przycisk = "SUB";
            else if (MOVButton.IsChecked == true)
                przycisk = "MOV";

            if (ARG1Val.Text == "" | ARG2Val.Text == "")
                MessageBox.Show("Two arguments required");
            else if (isProperRegister(ARG1Val.Text) == true && isProperRegister(ARG2Val.Text) == true)
            {
                OutputTextBox.Text = OutputTextBox.Text + przycisk + " " + ARG1Val.Text + "," + ARG2Val.Text + "\n";
                new_command_length = OutputTextBox.Text.Length - original_length;
                new_command_added = true;
            }
            else
            {
                ARG1Val.Text = "";
                ARG2Val.Text = "";
                MessageBox.Show("Wrong argument!!! Available arguments: " + String.Join(", ", registerList.ToArray())); 
            }
                








        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            if (OutputTextBox.Text.Length - new_command_length > 0)
            {
                if (new_command_added)
                {
                    OutputTextBox.Text = OutputTextBox.Text.Remove(OutputTextBox.Text.Length - new_command_length);
                    new_command_added = false;
                }
                else
                    MessageBox.Show("Only the last line can be removed.");
            }
            else
                MessageBox.Show("Command list is empty - nothing to remove.");
        }

        private void SaveButton_Click(object sender, RoutedEventArgs e)
        {
            string path = @"D:\Tomek\Szkoła\Semestr 6\Architektura Systemów Komputerowych\ASK\Zadanie 1\C#\code.txt";
            File.WriteAllText(path, OutputTextBox.Text);
            MessageBox.Show("Succesfully saved.");
        }

        private void LoadButton_Click(object sender, RoutedEventArgs e)
        {
            string path = @"D:\Tomek\Szkoła\Semestr 6\Architektura Systemów Komputerowych\ASK\Zadanie 1\C#\code.txt";
            OutputTextBox.Text = File.ReadAllText(path);

        }

        private void ARG1Val_TextChanged(object sender, TextChangedEventArgs e)
        {

        }
    }
}