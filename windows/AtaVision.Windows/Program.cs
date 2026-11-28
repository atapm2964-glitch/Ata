using Microsoft.Web.WebView2.Core;
using Microsoft.Web.WebView2.WinForms;

namespace AtaVision.Windows;

/// <summary>
/// AtaVision 81 Windows shell (WebView2).
/// Serves the bundled offline HTML at the fixed virtual-host origin
/// https://appassets.atavision.test/assets/index.html (unchanged from v80,
/// so UserData survives the upgrade). UserData lives in
/// %LOCALAPPDATA%\AtaVision\WindowsDesktop\UserData.
/// </summary>
internal static class Program
{
    private const string VirtualHost = "appassets.atavision.test";
    private const string StartUrl = "https://appassets.atavision.test/assets/index.html";

    [STAThread]
    private static void Main()
    {
        ApplicationConfiguration.Initialize();

        var assetsDir = Path.Combine(AppContext.BaseDirectory, "assets");
        var userDataDir = Path.Combine(
            Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
            "AtaVision", "WindowsDesktop", "UserData");
        Directory.CreateDirectory(userDataDir);

        using var form = new Form
        {
            Text = "AtaVision",
            WindowState = FormWindowState.Maximized,
            StartPosition = FormStartPosition.CenterScreen,
        };

        var webView = new WebView2 { Dock = DockStyle.Fill };
        form.Controls.Add(webView);

        form.Load += async (_, _) =>
        {
            var env = await CoreWebView2Environment.CreateAsync(null, userDataDir);
            await webView.EnsureCoreWebView2Async(env);
            webView.CoreWebView2.SetVirtualHostNameToFolderMapping(
                VirtualHost, assetsDir, CoreHostMappingAccessKind.Allow);
            webView.Source = new Uri(StartUrl);
        };

        Application.Run(form);
    }
}
