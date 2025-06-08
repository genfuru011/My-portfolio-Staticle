Rails.application.routes.draw do
  # Homepage
  root "pages#index"
  
  # Blog routes - equivalent to Flask routes
  get "blog", to: "blog#index"
  get "blog/category/:category", to: "blog#category", as: :blog_category
  get "blog/tag/:tag", to: "blog#tag", as: :blog_tag
  get "blog/:slug", to: "blog#show", as: :blog_post
  
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Render dynamic PWA files from app/views/pwa/* (remember to link manifest in application.html.erb)
  # get "manifest" => "rails/pwa#manifest", as: :pwa_manifest
  # get "service-worker" => "rails/pwa#service_worker", as: :pwa_service_worker
end
