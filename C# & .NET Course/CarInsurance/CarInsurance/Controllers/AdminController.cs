using CarInsurance.Models;
using CarInsurance.ViewModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace CarInsurance.Controllers
{
    public class AdminController : Controller
    {
        // GET: Admin
        public ActionResult Index()
        {
            using (InsuranceEntities db = new InsuranceEntities())
            {
                List<Table> insuredPerson = db.Tables.Where(x => x.Quote >= 0).ToList();
                List<InsuranceVM> insurees = new List<InsuranceVM>();
                foreach (Table person in insuredPerson)
                {
                    InsuranceVM insurer = new InsuranceVM
                    {
                        FirstName = person.FirstName,
                        LastName = person.LastName,
                        EmailAddress = person.EmailAddress,
                        Quote = person.Quote
                    };
                    insurees.Add(insurer);
                }
                return View(insurees);
            }
        }
    }
}
