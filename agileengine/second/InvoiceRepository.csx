using System;
using System.Collections.Generic;
using System.Linq;

public class Invoice
{
    // A unique numerical identifier of an invoice (mandatory)
    public int Id { get; set; }
    // A short description of an invoice (optional).
    public string Description { get; set; }
    // A number of an invoice e.g. 134/10/2018 (mandatory).
    public string Number { get; set; }
    // An issuer of an invoice e.g. Metz-Anderson, 600  Hickman Street,Illinois (mandatory).
    public string Seller { get; set; }
    // A buyer of a service or a product e.g. John Smith, 4285  Deercove Drive, Dallas (mandatory).
    public string Buyer { get; set; }
    // A date when an invoice was issued (mandatory).
    public DateTime CreationDate { get; set; }
    // A date when an invoice was paid (optional).
    public DateTime? AcceptanceDate { get; set; }
    // A collection of invoice items for a given invoice (can be empty but is never null).
    public IList<InvoiceItem> InvoiceItems { get; set; }

    public Invoice()
    {
        InvoiceItems = new List<InvoiceItem>();
    }
}

public class InvoiceItem
{
    // A name of an item e.g. eggs.
    public string Name { get; set; }
    // A number of bought items e.g. 10.
    public uint Count { get; set; }
    // A price of an item e.g. 20.5.
    public decimal Price { get; set; }
}

public interface IInvoiceRepository { }

public class InvoiceRepository : IInvoiceRepository
{
    private readonly IQueryable<Invoice> _invoices;

    public InvoiceRepository(IQueryable<Invoice> invoices)
    {
        if (invoices is null) {
            throw new ArgumentNullException();
        }
        _invoices = invoices;
    }

    /// <summary>
    /// Should return a total value of an invoice with a given id. If an invoice does not exist null should be returned.
    /// </summary>
    /// <param name="invoiceId"></param>
    /// <returns></returns>
    public decimal? GetTotal(int invoiceId)
    {
        return _invoices
            .Where(i => i.Id == invoiceId)
            .SingleOrDefault().InvoiceItems
                ?.Sum(i => i.Count * i.Price);
    }

    /// <summary>
    /// Should return a total value of all unpaid invoices.
    /// </summary>
    /// <returns></returns>
    public decimal GetTotalOfUnpaid()
    {
        return _invoices
            .Where(i => i.AcceptanceDate == null)
            .Sum(u => u.InvoiceItems
                .Sum(i => i.Count * i.Price));
    }

    /// <summary>
    /// Should return a dictionary where the name of an invoice item is a key and the number of bought items is a value.
    /// The number of bought items should be summed within a given period of time (from, to). Both the from date and the end date can be null.
    /// * Assumptions:
    /// * If <paramref>from</paramref> is null, it is set to <see cref="DateTime.MinValue" /> so only invoices up to <paramref>to</paramref> are included.
    /// * If <paramref>to</paramref> is null, it is set to <see cref="DateTime.MaxValue" /> only invoices since <paramref>from</paramref> are included.
    /// * If both <paramref>from</paramref> and <paramref>to</paramref> are null, all invoices are included.
    /// </summary>
    /// <param name="from"></param>
    /// <param name="to"></param>
    /// <returns></returns>
    public IReadOnlyDictionary<string, long> GetItemsReport(DateTime? from, DateTime? to)
    {
        if (from is null) {
            from = DateTime.MinValue;
        }
        if (to is null) {
            to = DateTime.MaxValue;
        }

        return _invoices
            .Where(i => i.AcceptanceDate >= from && i.AcceptanceDate <= to)
            .SelectMany(i => i.InvoiceItems)
            .GroupBy(i => i.Name)
            .ToDictionary(g => g.Key, g => (long)g.Sum(i => i.Count));
    }
}

// my quick test case
var invoices = new List<Invoice> {
    new Invoice {
        Id = 1,
        CreationDate = DateTime.Now,
        AcceptanceDate = DateTime.Now,
        InvoiceItems = new List<InvoiceItem> {
            new InvoiceItem {
                Name = "Egg",
                Count = 5,
                Price = 2.5m
            },
            new InvoiceItem {
                Name = "Apple",
                Count = 1,
                Price = 4
            }
        }
    },
    new Invoice {
        Id = 2,
        CreationDate = DateTime.Now,
        AcceptanceDate = DateTime.Now,
        InvoiceItems = new List<InvoiceItem> {
            new InvoiceItem {
                Name = "Egg",
                Count = 10,
                Price = 2.5m
            },
            new InvoiceItem {
                Name = "Orange",
                Count = 3,
                Price = 3.25m
            }
        }
    },
    new Invoice {
        Id = 3,
        CreationDate = DateTime.Now,
        AcceptanceDate = DateTime.Now,
        InvoiceItems = new List<InvoiceItem> {
            new InvoiceItem {
                Name = "Egg",
                Count = 8,
                Price = 2.5m
            },
            new InvoiceItem {
                Name = "Apple",
                Count = 2,
                Price = 4
            }
        }
    },
};

// my quick test
var repository = new InvoiceRepository(invoices.AsQueryable());
var dictionary = repository.GetItemsReport(null, null);
foreach (var item in dictionary) {
    Console.WriteLine($"{item.Key}: {item.Value}");
}