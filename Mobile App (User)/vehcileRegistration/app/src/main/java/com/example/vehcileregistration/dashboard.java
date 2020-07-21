package com.example.vehcileregistration;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;

import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;

import com.google.android.material.bottomnavigation.BottomNavigationView;

public class dashboard extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);
        BottomNavigationView bnv=findViewById(R.id.bottomnavid);
        bnv.setOnNavigationItemSelectedListener(botnav);
        getSupportFragmentManager().beginTransaction().replace(R.id.dashboardframe,new homejava()).commit();

    }

    private BottomNavigationView.OnNavigationItemSelectedListener botnav=new BottomNavigationView.OnNavigationItemSelectedListener() {
        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            Fragment selectedfragement =null;
            switch (item.getItemId())
            {
                case R.id.homeitem :
                    selectedfragement =new homejava();
                    break;
                case R.id.additem :
                    selectedfragement=new addjava();
                    break;
                case R.id.deleteitem :
                    selectedfragement=new deletejava();
                    break;
                case R.id.applyitem :
                    selectedfragement=new applyjava();
                    break;

            }
            getSupportFragmentManager().beginTransaction().replace(R.id.dashboardframe,selectedfragement).commit();
            return true;
        }
    };

    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater=getMenuInflater();
        inflater.inflate(R.menu.top_nav,menu);
        return true;
    }

}
