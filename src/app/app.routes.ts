import { Routes } from '@angular/router';

import { HomeComponent } from './Pages/home/home.component';
import { ContactComponent } from './Pages/contact/contact.component';
import { AboutComponent } from './Pages/about/about.component';
import { HelpComponent } from './Pages/help/help.component';
import { ConfigurationComponent } from './Pages/configuration/configuration.component';


//Paginas de configuración
import { DockerfileComponent } from './Pages/configuration/dockerfile/dockerfile.component';
import { NginxComponent } from './Pages/configuration/nginx/nginx.component';

export const routes: Routes = [
    { path: '', component: HomeComponent},
    { path: 'Configuration', component: ConfigurationComponent,children:[
        {path: 'Dockerfile', component:DockerfileComponent },
        {path: 'Ngix', component:NginxComponent }
    ] },
    { path: 'about', component: AboutComponent },
    { path: 'contact', component: ContactComponent},
    { path: 'help', component: HelpComponent },
    { path: '**', redirectTo: '', pathMatch: 'full' }
];