## Reviews on Trying out Symfony(2)
#### Doctrine
Symfony does not have core component that works with Databases. Instead, it uses third-party library called Doctrine.
Doctrine allows building database schema through `Entity Class`, retrieving it, and more.
Symfony commands through bin/console can connect to various functionalities of Doctrine.

#### Trailing `\` Problem
Symfony routing will cause `401` error when there is a trailing slash in the url. To solve it, you should add additional controller for redirections as shown [here](https://symfony.com/doc/current/routing/redirect_trailing_slash.html).

```
// src/AppBundle/Controller/RedirectingController.php
namespace AppBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Request;

class RedirectingController extends Controller
{
    public function removeTrailingSlashAction(Request $request)
    {
        $pathInfo = $request->getPathInfo();
        $requestUri = $request->getRequestUri();

        $url = str_replace($pathInfo, rtrim($pathInfo, ' /'), $requestUri);

        return $this->redirect($url, 301);
    }
}
```
