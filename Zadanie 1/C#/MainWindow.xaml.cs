﻿using System;
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

        // Variable to calculate how many characters should be removed from code string
        int new_command_length = 0;

        // Variable for counting lines of assembler code
        uint code_lines = 0;

        // Bool value to check if a new line was recently added to program - if so, enable removing last line
        bool new_command_added = false;

        Register register = new Register();

        // Clear all registers
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

        // List of available arguments
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

        private void RunButton_Click(object sender, RoutedEventArgs e)
        {
            Char[] separators = { '\n', ' ', ',' };
            String[] lines = OutputTextBox.Text.Split(separators, StringSplitOptions.RemoveEmptyEntries);
            MessageBox.Show(lines[0] + "\n" + lines[1] + "\n" + lines[2] + "\n" + lines[3]);
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

        // Reset all variables and text boxes
        private void ClearButton_Click(object sender, RoutedEventArgs e)
        {
            OutputTextBox.Text = "";
            code_lines = 0;
            registersReset();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        { 
            int original_length = OutputTextBox.Text.Length;

            // Check which command is selected
            string przycisk = "";
            if (ADDButton.IsChecked == true)
                przycisk = "ADD";
            else if (SUBButton.IsChecked == true)
                przycisk = "SUB";
            else if (MOVButton.IsChecked == true)
                przycisk = "MOV";
            
            // Add new line of code, validate arguments before adding
            if (ARG1Val.Text == "" | ARG2Val.Text == "")
                MessageBox.Show("Two arguments required");
            else if (isProperRegister(ARG1Val.Text) == true && isProperRegister(ARG2Val.Text) == true)
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
                MessageBox.Show("Wrong argument!!! Available arguments: " + String.Join(", ", registerList.ToArray())); 
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
        private void Button_Click_2(object sender, RoutedEventArgs e)
        { 
        
        }

    }
}